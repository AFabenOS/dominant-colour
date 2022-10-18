from behave import *
import os
from app.video_downloader import YoutubeVideoDownloader

@given('a valid YouTube video URL is provided to the program')
def create_yt_url(context):
    yt_url = 'https://www.youtube.com/watch?v=icPHcK_cCF4'
    context.video_downloader = YoutubeVideoDownloader(yt_url)

@when('video downloader is run')
def start_video_download(context):
    context.video_downloader.download_video()

@then('an .mp4 file should be saved to the specified raw_videos directory')
def test_video_saved(context):
    file_location = r'raw_videos/'
    file_path = os.path.join(file_location, 'Countdown 5 seconds timer.mp4')
    assert os.path.exists(file_path)