import cv2
from services.drowsiness.DrowsinessDetector import DrowsinessDetector
from services.headpose.HeadposeDetector import HeadposeDetector
from services.emotion.Engine.EmotionDetector import EmotionDetector


class VisualFocusMeter:
    def __init__(self):
        self.drowsiness_detector = DrowsinessDetector()
        self.headpose_detector = HeadposeDetector()
        self.emotion_detector = EmotionDetector()

        self.DROWSINESS_PERCENTAGE = 1 / 3
        self.HEADPOSE_PERCENTAGE = 1 / 3
        self.EMOTION_PERCENTAGE = 1 / 3

    def get_visual_focus(self, image):
        drowsiness = self.drowsiness_detector.get_drowsiness(image)
        unfocusness, image = self.headpose_detector.get_unfocus_headpose_percentage(
            image
        )
        emotion = self.emotion_detector.get_emotional_focus(image)

        drowsiness_cofficient = 0 if drowsiness else 1
        headpose_coffiecient = 1 - unfocusness if unfocusness is not None else 0
        emotion_coffiecient = 1 if emotion else 0

        focus_amount = (
            drowsiness_cofficient * self.DROWSINESS_PERCENTAGE
            + headpose_coffiecient * self.HEADPOSE_PERCENTAGE
            + emotion_coffiecient * self.EMOTION_PERCENTAGE
        )

        return focus_amount

    def mark_image(self, image):
        drowsiness_image = self.drowsiness_detector.mark_image(image)
        _, headpose_image = self.headpose_detector.detect_headpose(drowsiness_image)
        emotion = self.emotion_detector.detect_emotion(image)

        # label image with emotion on top left
        cv2.putText(
            headpose_image,
            emotion,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
            cv2.LINE_AA,
        )

        return headpose_image


# focusmeter = VisualFocusMeter()

# sample_image = cv2.imread("sample/sample3.jpg")
# result = focusmeter.get_visual_focus(sample_image)
# print(result)
