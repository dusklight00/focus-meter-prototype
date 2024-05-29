from visual_focus import VisualFocusMeter
import cv2

focus_meter = VisualFocusMeter()

VIDEO_PATH = "output.mp4"

capture = cv2.VideoCapture(VIDEO_PATH)
visual_focus_meter = VisualFocusMeter()

while True:
    ret, frame = capture.read()

    if ret:
        focus = visual_focus_meter.get_visual_focus(frame)
        print(focus)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break