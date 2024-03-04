from pytube import YouTube

def download_mp3(video_url, destination_folder):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        mp3_file = audio_stream.download(output_path=destination_folder)
        print("MP3 downloaded successfully!")
        return mp3_file
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    destination_folder = input("Enter the destination folder path: ")
    download_mp3(video_url, destination_folder)
