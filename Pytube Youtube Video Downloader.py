from pytube import YouTube
from sys import argv
#link = argv[1]#add url in quote marks in terminal and run
#url = input('Please provide youtube link: ')
#yt = YouTube(link)
yt = YouTube(input('Please provide youtube link: '), use_oauth=True, allow_oauth_cache=True)
#print("Title:", yt.title)
#print("View:", yt.views)
#print('View: ', yt.streams.filter(res = 1080p, progressive = 'True',type, ))
#for video download
Video = yt.streams.get_highest_resolution()
#Video = yt.streams.filter(progressive=True).last()
##Video.download('/Users/philipsenn/Downloads/PROGRAMMING/PYTHON/Youtube/CONVERT')
#R = yt.streams.all()
#for i in R:
 #   print(i)
#yt.streams.get_by_itag(137).download('/Users/philipsenn/Downloads/PROGRAMMING/PYTHON/Youtube/CONVERT')
#Video = yt.streams.get_highest_resolution().download(output_path=save_folder_path + os.sep + name + os.sep, filename=name + f"{index}.mp4")
Video.download('/Users/philipsenn/Downloads/PROGRAMMING/PYTHON/Youtube/CONVERT')#store path
#for audio download
#Audio = yt.streams.get_audio_only()
#Audio.download('/Users/philipsenn/Downloads/PROGRAMMING/PYTHON/Youtube')
