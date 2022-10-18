@check-url-returns-valid-filename-and-location
Feature: Providing a URL to the program
    Scenario: Run a simple check to ensure a video gets saved to the correct location with the correct filename
        Given a valid YouTube video URL is provided to the program
            | URL                                         |
            | https://www.youtube.com/watch?v=icPHcK_cCF4 |
            # | https://www.youtube.com/watch?v=PUunRgUkRjQ |
        When video downloader is run
        Then an .mp4 file should be saved to the specified raw_videos directory
    
    Scenario: Provide an invalid URL and see how the issue is handled
        Given an invalid URL is provided to the program
        When the video downloader is run
        Then an error message should be returned instructing the user of what to do
        