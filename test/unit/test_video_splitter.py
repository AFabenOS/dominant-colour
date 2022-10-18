import pytest
import os

from app.video_downloader import YoutubeVideoDownloader
from app.video_splitter import VideoFrameSplitter

class TestVideoSplitter:

    @pytest.mark.parametrize(
        #Input, #Output
        'file_location',
        [
            r'test_video_frames/'
        ]
    )

    def test_video_frames_directory_exists(self, file_location):
        # Download the video to a test file
        yt_url = 'https://www.youtube.com/watch?v=icPHcK_cCF4'
        ydl_opts = {'outtmpl': 'test_video_frames/%(title)s.%(ext)s'}
        test_video = YoutubeVideoDownloader(yt_url, ydl_opts)
        test_video.download_video()

        # Split the frames into the file
        test_path = VideoFrameSplitter(path = r'test_videos/', frames_path = r'test_video_frames/')
        test_path.get_video_as_frames()

        test_path = r'test_video_frames/'
        assert os.path.exists(test_path)


    def test_image_file_in_frames_directory_exists(self):
        # Download the video to a test file
        yt_url = 'https://www.youtube.com/watch?v=icPHcK_cCF4'
        ydl_opts = {'outtmpl': 'test_video_frames/%(title)s.%(ext)s'}
        test_video = YoutubeVideoDownloader(yt_url, ydl_opts)
        test_video.download_video()

        test_image_file_exists_in_path = VideoFrameSplitter(path = r'test_videos/', frames_path = r'test_video_frames/')
        test_image_file_exists_in_path.get_video_as_frames()

        test_video_frames_location = r'test_video_frames/'
        assert '0.png' in os.listdir(test_video_frames_location)


# Future testing needs to handle more than one file in the raw_videos directory
# What to do if there's more than one - an ability to select the desired file

