import youtube_dl as yt

class YoutubeVideoDownloader():
    def __init__(self, yt_url, ydl_opts={
        'outtmpl': 'raw_videos/%(title)s.%(ext)s'}):
       # Sets the youtube url, and default information needed for processing
        self.yt_url = yt_url
        self.ydl_opts = ydl_opts

    def get_video_title_filename(self):
        # Turns the Youtube video title into a workable filename
        with yt.YoutubeDL(self.ydl_opts) as ydl:
            meta_info = ydl.extract_info(
                self.yt_url, download=False
            )
        video_filename = '%s' %(meta_info['title'])
        return video_filename

    def get_youtube_video_download(self, video_filename):
        # Downloads the YouTube video
        # Note: youtube_dl automatically checks if the video is downloaded
        with yt.YoutubeDL(self.ydl_opts) as ydl:
            print("Attempting to Download:", video_filename)
            ydl.download([self.yt_url])
            print("Successfully download:", video_filename)
    
    def download_video(self):
        # Calls all methods needed to download the video and provide a filename
        yt_filename = self.get_video_title_filename()
        downloaded_video = self.get_youtube_video_download(yt_filename)
        return downloaded_video

if __name__ == '__main__':
    # This will only execute if the program is ran here and not in main.py
    yt_url = 'https://www.youtube.com/watch?v=H9154xIoYTA'
    test_attempt = YoutubeVideoDownloader(yt_url)
    test_attempt.download_video()