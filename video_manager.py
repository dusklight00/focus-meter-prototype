# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import WriteGear

class VideoInstance:
    def __init__(self, video_path):
        self.writer = WriteGear(output=video_path)
    
    def add_frame(self, frame):
        self.writer.write(frame)
