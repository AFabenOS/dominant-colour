import pytest
import os

from app.video_downloader import YoutubeVideoDownloader

class TestYoutubeVideoDownloader:

    # test_url = 'https://www.youtube.com/watch?v=icPHcK_cCF4'
    # Test that 
    @pytest.mark.parametrize(
        # Input, # Output
        'test_url, expected_output',
        [
            ('https://www.youtube.com/watch?v=icPHcK_cCF4', 'Countdown 5 seconds timer')
        ],
    )

    def test_get_video_title(self, test_url, expected_output):
        get_yt_video_title = YoutubeVideoDownloader(test_url)

        output = get_yt_video_title.get_video_title_filename()

        assert type(output) == type(expected_output)
        assert output == expected_output


    @pytest.mark.parametrize(
        'file_location',
        [
            r'raw_videos/'
        ]
    )

    def test_get_youtube_video_download_file_exists(self, file_location):
        yt_url = 'https://www.youtube.com/watch?v=icPHcK_cCF4'
        ydl_opts = {'outtmpl': 'test_videos/%(title)s.%(ext)s'}
        check_video_exists_in_folder = YoutubeVideoDownloader(yt_url, ydl_opts)


        check_video_exists_in_folder.download_video()

        path = os.path.join(file_location, 'Countdown 5 seconds timer.mp4')
        assert os.path.exists(path)
        
        os.remove(path)