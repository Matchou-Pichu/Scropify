import os
import re
import music_tag
from pytubefix import YouTube
from pytubefix.cli import on_progress
from yt_dlp import YoutubeDL

def safe_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '', name)

url = 'PASTE YOUTUBE URLS HERE BETWEEN APOSTROPHE'
track_name = safe_filename('TITLE OF THE SONG')  # Use anti slash if it has non-latin character. Ex : 'It\'s okay'

output_template = os.path.join('_ManualDowloaderManFolder\\', track_name + ".%(ext)s")

ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'quiet': True,
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '192',
            }],
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

pathfile = '_ManualDowloaderManFolder' + '\\' + track_name + '.m4a'
print("Checking file:", pathfile)
print("Exists:", os.path.exists(pathfile))
print("Size:", os.path.getsize(pathfile) if os.path.exists(pathfile) else "N/A")

# Metadata editing
f = music_tag.load_file(pathfile)
f['title'] = track_name
f['album'] = 'ENTER ALBUM NAME'
f['albumartist'] = 'ENTER ALBUM ARTIST'
f['artist'] = 'ENTER ARTIST ON THE TRACK'
f['totaltracks'] = 1 # IMPORTANT ENTER THE NUMBER OF SONG IN THE ALBUM
f['tracknumber'] = 1 # IMPORTANT ENTER THE NUMBER THAT THE TRACK HAS IN THE ALBUM
cover_path = '_cover\\RECOVER THE ID FROM _cover FOLDER.jpg'
with open(cover_path, 'rb') as img_in:
    f['artwork'] = img_in.read()
f.save()