import keras
from keras.layers import Input, Flatten, Dropout, Activation
from keras.layers import Dense
from keras.layers import Conv1D, MaxPooling1D
from keras.models import Sequential
from sklearn.model_selection import train_test_split
import librosa
import scipy.io.wavfile
import numpy as np
import os
import json
import matplotlib.pyplot as plt
from tqdm import tqdm
from services.vocal_emotion.utils import auto_pad
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import pickle
from tensorflow.python.keras.utils import np_utils


class VocalEmotionDetection:
    def __init__(
        self,
        load_cache_dataset=True,
        load_cache_model=True,
        save_cache_model=True,
        load_cache_encoder=True,
        save_cache_encoder=True,
    ):
        self.CACHE_MODEL_FILENAME = "model.h5"
        self.CACHE_ENCODER_FILENAME = "encoder.pkl"
        self.CACHE_FEATURES_DATASET_FILENAME = "features.json"
        self.CACHE_LABELS_DATASET_FILENAME = "labels.json"

        self.is_save_cache_model = save_cache_model
        self.is_save_cache_encoder = save_cache_encoder

        # Loading Model
        if load_cache_model and os.path.exists(self.CACHE_MODEL_FILENAME):
            self.model = self._load_cache_model()
        else:
            self.model = self._generate_model()

        # Loading Encoder
        if load_cache_encoder and os.path.exists(self.CACHE_ENCODER_FILENAME):
            self.encoder = self._load_cache_encoder()
        else:
            self.encoder = LabelEncoder()

        # Loading Dataset
        if (
            load_cache_dataset
            and os.path.exists(self.CACHE_FEATURES_DATASET_FILENAME)
            and os.path.exists(self.CACHE_LABELS_DATASET_FILENAME)
        ):
            self.features = json.load(open("features.json", "r"))
            self.labels = json.load(open("labels.json", "r"))
        else:
            self.features, self.labels = self._generate_dataset(
                "./services/vocal_emotion/dataset"
            )
            json.dump(self.features, open("features.json", "w"))
            json.dump(self.labels, open("labels.json", "w"))

        self.history = None

    def _generate_model(self):
        model = Sequential()
        model.add(Conv1D(256, 5, padding="same", input_shape=(216, 1)))
        model.add(Activation("relu"))
        model.add(Conv1D(128, 5, padding="same"))
        model.add(Activation("relu"))
        model.add(Dropout(0.1))
        model.add(MaxPooling1D(pool_size=(8)))
        model.add(
            Conv1D(
                128,
                5,
                padding="same",
            )
        )
        model.add(Activation("relu"))
        # model.add(Conv1D(128, 5,padding='same',))
        # model.add(Activation('relu'))
        # model.add(Conv1D(128, 5,padding='same',))
        # model.add(Activation('relu'))
        # model.add(Dropout(0.2))
        model.add(
            Conv1D(
                128,
                5,
                padding="same",
            )
        )
        model.add(Activation("relu"))
        model.add(Flatten())
        model.add(Dense(16))
        model.add(Activation("softmax"))

        optimizer = keras.optimizers.RMSprop(learning_rate=0.00001, decay=1e-6)
        model.compile(
            loss="categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"]
        )
        model.summary()

        return model

    def _generate_label_wavefiles(self, wavfile_path):
        filename = wavfile_path.split("/")[-1].split(".")[0]
        parameters = filename.split("-")
        emotion_id = int(parameters[2])
        actor_id = int(parameters[6])
        is_female = actor_id % 2 == 0

        emotion = None
        if emotion_id == 1:
            emotion = "neutral"
        elif emotion_id == 2:
            emotion = "calm"
        elif emotion_id == 3:
            emotion = "happy"
        elif emotion_id == 4:
            emotion = "sad"
        elif emotion_id == 5:
            emotion = "angry"
        elif emotion_id == 6:
            emotion = "fearful"
        elif emotion_id == 7:
            emotion = "disgust"
        elif emotion_id == 8:
            emotion = "surprised"

        return {"emotion": emotion, "gender": "female" if is_female else "male"}

    def _generate_dir_labels(self, wavfile_dir):
        labels = []
        for filename in os.listdir(wavfile_dir):
            label = self.generate_label_wavefiles(wavfile_dir + "/" + filename)
            labels.append(label)
        return labels

    def _generate_feature(self, wavfile_path):
        x, sampling_rate = librosa.load(
            wavfile_path, res_type="kaiser_fast", duration=2.5, sr=22050 * 2, offset=0.5
        )
        sampling_rate = np.array(sampling_rate)
        mfccs = librosa.feature.mfcc(y=x, sr=sampling_rate, n_mfcc=13)
        feature = np.mean(mfccs, axis=0)
        return feature.tolist()

    def _generate_dir_features(self, dir_path):
        features = []
        labels = []
        for filename in os.listdir(dir_path):
            wave_path = dir_path + "/" + filename
            feature = self._generate_feature(wave_path)
            label = self._generate_label_wavefiles(wave_path)
            label_name = label["emotion"] + "__" + label["gender"]
            features.append(feature)
            labels.append(label_name)
        return features, labels

    def _generate_dataset(self, dataset_path):
        dataset_features = []
        dataset_labels = []
        for dir in tqdm(os.listdir(dataset_path)):
            dir_path = dataset_path + "/" + dir
            features, labels = self._generate_dir_features(dir_path)
            dataset_features += features
            dataset_labels += labels

        return dataset_features, dataset_labels

    def _generate_spectrogram(self, wavefile_path):
        sampling_rate, x = scipy.io.wavfile.read(wavefile_path)
        nstep = int(sampling_rate * 0.01)
        nwin = int(sampling_rate * 0.03)
        nfft = nwin
        window = np.hamming(nwin)
        nn = range(nwin, len(x), nstep)
        X = np.zeros((len(nn), nfft // 2))

        for i, n in enumerate(nn):
            xseg = x[n - nwin : n]
            z = np.fft.fft(window * xseg, nfft)
            X[i, :] = np.log(np.abs(z[: nfft // 2]))

        return X.T

    def show_spectrogram(self, wavefile_path):
        image = self._generate_spectrogram(wavefile_path)
        plt.imshow(image, interpolation="nearest", origin="lower", aspect="auto")
        plt.show()

    def _one_hot_encode(self, labels):
        return np_utils.to_categorical(self.encoder.fit_transform(labels))

    def _one_hot_decode(self, labels):
        return self.encoder.inverse_transform(labels)

    def train(self):
        train_features, test_features, train_labels, test_labels = train_test_split(
            self.features, self.labels, test_size=0.2, random_state=42
        )

        train_features_padded = auto_pad(train_features)
        test_features_padded = auto_pad(test_features)

        train_labels = self._one_hot_encode(train_labels)
        test_labels = self._one_hot_encode(test_labels)

        self._save_cache_encoder()

        self.history = self.model.fit(
            train_features_padded,
            train_labels,
            batch_size=16,
            epochs=100,
            validation_data=(test_features_padded, test_labels),
        )

        if self.is_save_cache_model:
            self._save_cache_model()

        return self.history

    def quick_train(self):
        train_features, test_features, train_labels, test_labels = train_test_split(
            self.features, self.labels, test_size=0.2, random_state=42
        )

        train_features_padded = auto_pad(train_features)
        test_features_padded = auto_pad(test_features)

        train_labels = self._one_hot_encode(train_labels)
        test_labels = self._one_hot_encode(test_labels)

        self._save_cache_encoder()

        self.history = self.model.fit(
            train_features_padded,
            train_labels,
            batch_size=16,
            epochs=10,
            validation_data=(test_features_padded, test_labels),
        )

        if self.is_save_cache_model:
            self._save_cache_model()

        return self.history

    def show_history(self):
        if self.history is None:
            print("Please train the model first")
            return
        plt.plot(self.history.history["loss"])
        plt.plot(self.history.history["val_loss"])
        plt.title("model loss")
        plt.ylabel("loss")
        plt.xlabel("epoch")
        plt.legend(["train", "test"], loc="upper left")
        plt.show()

    def _save_cache_model(self):
        self.model.save(self.CACHE_MODEL_FILENAME)

    def _load_cache_model(self):
        return load_model(self.CACHE_MODEL_FILENAME)

    def _save_cache_encoder(self):
        with open(self.CACHE_ENCODER_FILENAME, "wb") as file:
            pickle.dump(self.encoder, file)

    def _load_cache_encoder(self):
        with open(self.CACHE_ENCODER_FILENAME, "rb") as file:
            return pickle.load(file)

    def predict_wavefile(self, wavfile_path):
        MAX_PAD = 216
        feature = self._generate_feature(wavfile_path)
        feature_padded = np.pad([feature], (0, MAX_PAD - len(feature)), "constant")
        prediction = self.model.predict(feature_padded)[0]
        label = self._one_hot_decode([np.argmax(prediction)])[0]
        return str(label)

    def predict_wavefunction(self, x, sampling_rate):
        MAX_PAD = 216
        sampling_rate = np.array(sampling_rate)
        mfccs = librosa.feature.mfcc(y=x, sr=sampling_rate, n_mfcc=13)
        feature = np.mean(mfccs, axis=0).tolist()
        feature_padded = np.pad([feature], (0, MAX_PAD - len(feature)), "constant")
        prediction = self.model.predict(feature_padded)[0]
        label = self._one_hot_decode([np.argmax(prediction)])[0]
        return str(label)

    def check_focus_wavefile(self, wavefile_path):
        emotion = self.predict_wavefile(wavefile_path)
        emotion = str(emotion)
        is_focus = "neutral" in emotion or "sad" in emotion or "fearful" in emotion
        return is_focus


# AUDIO_PATH = "dataset/Actor_01/03-01-01-01-01-01-01.wav"

# detector = VocalEmotionDetection()
# detector.train()
# detector.show_history()

# x, sampling_rate = librosa.load(
#     AUDIO_PATH, res_type="kaiser_fast", duration=2.5, sr=22050 * 2, offset=0.5
# )
# result = detector.predict_wavefunction(x, sampling_rate)
# print(result)
