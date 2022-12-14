import time

from app.video_downloader import YoutubeVideoDownloader
from app.video_splitter import VideoFrameSplitter


from app.file_deleter import FileDeleter

if __name__ == '__main__':
    start_time = time.time()

    # This will only execute if the program is ran here and not in main.py
    yt_url = 'https://www.youtube.com/watch?v=H9154xIoYTA'

    wonderful_world_download = YoutubeVideoDownloader(yt_url)
    wonderful_world_download.download_video()

    wonderful_world_frames = VideoFrameSplitter()
    wonderful_world_frames.get_video_as_frames()




    # Future Andrew: This is the final command
    # remove_created_folders = FileDeleter()
    # remove_created_folders.remove_all_files()

    end_time = time.time()
    run_time = end_time - start_time