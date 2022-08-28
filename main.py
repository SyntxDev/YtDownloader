import pytube
link = input("Please enter video url: ")
video = pytube.YouTube(link)
path = input("Please enter path to download video: ")
stream = video.streams.first()
stream.download(path)
print("Video Downloaded")
