from concurrent.futures import ThreadPoolExecutor
from ffmpy3 import FFmpeg
import os


class FFUtil:

    def __init__(self, *args):
        self.videoPath = args[0]
        self.savePath = args[1]
        self.ffPath = args[2]

    def asyncTest(self):
        print(os.name)
        if self.ffPath.strip() == '':
            self.ffPath = "ffmpeg.exe" if os.name == 'nt' else "ffmpeg"

        ff = FFmpeg(
            inputs={self.videoPath: None},
            outputs={self.savePath: "-codec copy"},
            executable=self.ffPath,
        )
        print(ff.cmd)
        ff.run()
        return "success"

    def run(self, callback):
        pool = ThreadPoolExecutor(5)
        v = pool.submit(self.asyncTest)
        v.add_done_callback(callback)


