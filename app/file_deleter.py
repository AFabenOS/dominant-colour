import os
import shutil

class FileDeleter:
    # Class that deletes all files created when program is executed. 
    def __init__(self, video_path = r'raw_videos/', frames_path = r'video_frames/'):
        self.video_path = video_path
        self.frames_path = frames_path

    def remove_video_file(self):
        if self.video_path:
            # os.remove(self.video_path)
            shutil.rmtree(self.video_path)
    
    def remove_frames_file(self):
        if self.frames_path:
            # os.remove(self.frames_path)
            shutil.rmtree(self.frames_path)

    def remove_all_files(self):
        self.remove_video_file()
        self.remove_frames_file()

if __name__ == '__main__':
    test_removal = FileDeleter()
    test_removal.remove_all_files()