from pytube import YouTube 

save_path = "E:/python"

link = "https://youtu.be/AtGih-K-7U0"

try:
    yt = YouTube(link)
except:
    print("Connection Error!")

mp4files = yt.filter('mp4')
yt.set_filname('Python downloader')
video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)

try:
    video.download(save_path)
except:
    print("An error occurred while downloading the file.")

print("Download complete chwck downloads.")
