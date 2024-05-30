import uuid
import numpy as np
import cv2
import base64

def generate_uuid():
    return str(uuid.uuid4())

def convert_base64_to_cv2(base64_string):
    base64_string = base64_string.split(",")[1]
    img_bytes = base64.b64decode(base64_string)
    img_arr = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    return img