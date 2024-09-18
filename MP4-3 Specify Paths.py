import os
from moviepy.editor import *
def MP4to3(mp4, mp3):
  File = AudioFileClip(mp4)
  File.write_audiofile(mp3)
  #FILETOCONVERT.close()
A = '/Users/philipsenn/Downloads/PROGRAMMING/PYTHON/Youtube/CONVERT/'
#A = input("Please provide path to source folder. It should end with '/'")
Z = '/Users/philipsenn/Downloads/PROGRAMMING/PYTHON/Youtube/CONVERTED/'
#Z = input("Please provide path to destination folder. It should end with '/'")
for i in os.listdir(A):#Use this if you are reading from the folder
  a = i.find('.mp4')
  b = i[:a]
  c = A + i
  d = Z + b + '.mp3'
  MP4to3(c, d)
 # e =+ 1
#print(f'{e} files converted successfully')
