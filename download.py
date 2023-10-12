from pytube import YouTube

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[94m'
RESET = '\033[0m'

print(BLUE + "Welcome to another-yt-downloader v1.0. This is a simple cli-application for \
downloading youtube videos and audio.")

def download(url, directory, audio):
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.filter(only_audio=audio).first()

    try:
        if (directory != ""):
            youtubeObject.download(output_path=directory)
        else: youtubeObject.download()

        print(RESET + "Download is completed successfully")
    except Exception as e:
        print(RESET + f"An error has occurred. {e}")


url = input(YELLOW + "Enter the YouTube video URL: ")
directory = input(YELLOW + "Enter the address to the directory: ")
audioStatus = input(YELLOW + "Do you want audio? Options are True/False: ").lower()

if audioStatus == "true":
    audio = True
else: audio= False


download(url, directory, audio)