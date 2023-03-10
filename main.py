from pytube import YouTube
import pathlib


def main():
    try:
        option = int(input("Where do you want to download it from? (1) URL or (2) FILE: "))
        if option == 1:
            url = input("Enter URL of youtube video: ")
            print("Enter the destination address (leave blank to save in current directory):")
            destination = input(" ") or '.'
            response = download_music(url, destination)
            print(response)
        elif option == 2:
            file = input("Enter name of file: ")
            print("Enter the destination address (leave blank to save in current directory):")
            destination = input(" ") or '.'
            with open(file, "r") as f:
                for row in f:
                    response = download_music(row, destination)
                    print(response)
        else:
            raise Exception("Invalid option")
    except:
        print("Enter a valid numeric option...")


def download_music(url: str, directory: str) -> str:
    try:
        yt = YouTube(str(url))
        video = yt.streams.filter(only_audio=True).first()
        destination = str(directory)
        out_file = video.download(output_path=destination)
        file = pathlib.Path(out_file)
        new_file = file.with_suffix(".mp3")
        file.rename(new_file)
        return f"{yt.title} has been successfully downloaded."
    except:
        return f"An error as occurred..."

if __name__ == "__main__":
   main() 
