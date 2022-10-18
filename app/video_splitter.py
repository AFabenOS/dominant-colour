import cv2
import os

class VideoFrameSplitter():
    def __init__(self, path = r'raw_videos/', frames_path = r'video_frames/'):
        self.path = path
        self.frames_path = frames_path

    def create_frames_directory(self):
    # Create a directory to save the frames in
        try:
            os.mkdir(self.frames_path)
            return self.frames_path
        except OSError:
            pass
    
    def get_video_file_path(self):
        # Retrieve the mp4 file name in the raw_videos directory
        file_list = []
        files_in_directory = os.listdir(self.path)
        for file in files_in_directory:
            file_list.append(file)
            
        if len(file_list) == 0:
            print("There are no files in this location.")
            pass
        
        elif len(file_list) > 1:
            # Eventually add ability to select which file to choose
            print("Please ensure only 1 file exists in this folder.")
            print("Please remove all files that are not the one you need")
            pass
        
        else:
            file_list = file_list[0]
            # need to prefix file_list with the directory so r'raw_videos/file_list'
            video_file_path = os.path.join(self.path, file_list)
            print(video_file_path)
            return video_file_path

    # need to combine the video file folder + video
    def extract_video_frames(self, video_file_location):

        video_capture = cv2.VideoCapture(video_file_location)
        count = 0
        print("Getting Frames.")
        while video_capture.isOpened():
            success, image = video_capture.read()
            if success:
                cv2.imwrite(os.path.join(self.frames_path, '%d.png') % count, image)
                count += 1
            else:
                break
        cv2.destroyAllWindows()
        video_capture.release()

    def get_video_as_frames(self):
        self.create_frames_directory()
        
        video_file_location = self.get_video_file_path()
        video_to_frames_converter = self.extract_video_frames(video_file_location)
        return video_to_frames_converter

if __name__ == '__main__':
    # This will only execute if the program is ran here and not in main.py
    test_attempt = VideoFrameSplitter()
    test_attempt.get_video_as_frames()