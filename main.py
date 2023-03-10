from pytube import YouTube
import pathlib

url = input("Enter URL of youtube video: ")
yt = YouTube(str(url))
video = yt.streams.filter(only_audio=True).first()
print("Enter the destination address (leave blank to save in current directory):")
destination = input(" ") or '.'
out_file = video.download(output_path=destination)
file = pathlib.Path(out_file)
new_file = file.with_suffix(".mp3")
file.rename(new_file)
print(yt.title + " has been successfully downloaded.")
