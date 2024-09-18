import os
from moviepy.editor import *
def MP4to3(mp4, mp3):
   File = AudioFileClip(mp4)
   File.write_audiofile(mp3)
   #FILETOCONVERT.close()
R = open('/Users/philipsenn/Downloads/PROGRAMMING/PYTHON/Youtube/AUDIO.txt', 'r')
for i in R:
   i = i.strip()
   v = '/Users/philipsenn/Downloads/PROGRAMMING/PYTHON/Youtube/CONVERT/' + str(i)
   e = v.find('.mp4')
   a = v[:e] + '.mp3'
   #print(a)
   MP4to3(v, a)
