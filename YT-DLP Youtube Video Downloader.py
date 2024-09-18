import yt_dlp
from sys import argv
url = argv[1]
#url = input('Please provide youtube link: ')

yt-dlp -S res,vcodec:h264,acodec:m4a,ext url
yt-dlp -S res,vcodec:h264,acodec:m4a,ext https://www.youtube.com/watch?v=I4a91ww1qsU

bash-3.2$ yt-dlp -x --audio-format mp3 -P ~/Downloads https://www.youtube.com/watch?v=eQBRFxb4-pA&list=PLyijK8r_zE5J1a5mrLxgxraLFRnNN5HDL&index=16