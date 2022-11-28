import os
import numpy as np
import cv2


class VideoReader:
    def __init__(self, video_file):
        self.video_file = video_file
        self.video = cv2.VideoCapture(self.video_file)

        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.num_images = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

        self.curr_time = self.video.get(cv2.CAP_PROP_POS_MSEC) #in millisec , from beginning of video file
        self.curr_image = self.video.get(cv2.CAP_PROP_POS_FRAMES)
        self.total_duration = self.get_video_duration()

    def get_video_duration(self):
        self.get_nth_image(self.num_images - 1)
        duration = self.curr_time
        self.reset()
        return duration

    def get_next_image(self):
        ret_val, img = self.video.read()
        self.curr_time = self.video.get(cv2.CAP_PROP_POS_MSEC)
        self.curr_image = self.video.get(cv2.CAP_PROP_POS_FRAMES)
        return ret_val, img

    def get_nth_image(self, n):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, n)
        return self.get_next_image()

    def reset(self):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.curr_time = self.video.get(cv2.CAP_PROP_POS_MSEC)
        self.curr_image = self.video.get(cv2.CAP_PROP_POS_FRAMES)
        return
