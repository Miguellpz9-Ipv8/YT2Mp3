from pytube import YouTube
import os
import subprocess

def download_mp3_from_youtube_list(list_file):
    if not os.path.exists("mp3_downloads"):
        os.makedirs("mp3_downloads")

    with open(list_file, "r") as file:
        video_urls = file.readlines()

    for url in video_urls:
        url = url.strip()
        try:
            video = YouTube(url)
            audio_stream = video.streams.filter(only_audio=True, file_extension="mp4").first()
            mp3_file_path = os.path.join("mp3_downloads", f"{video.title}.mp3")
            audio_stream.download(output_path="mp3_downloads", filename=video.title + ".mp3")

            print(f"Downloaded MP3: {video.title}.mp3")

        except Exception as e:
            print(f"Failed to download {url}: {e}")

input_list_file = input("Provide URL list: ")
download_mp3_from_youtube_list(input_list_file)
