import numbers
import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = 'C:\\Users\\Jhonchi\\Downloads'
print('''
=================================
    YOUTUBE PLAYLIST DOWNLOAD
=================================\n''')

string_url = input("Enter PlayList Youtube Link > ")
playlist = Playlist(string_url)

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
numbers = int(len(playlist.video_urls))

# physically downloading the audio track
print("=================================")
for video in playlist.videos:
    numbers = numbers - 1
    print(f"[ {numbers} ] {video.title}", end='\r')
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)
