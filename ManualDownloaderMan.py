import os
import re
import music_tag
from pytubefix import YouTube
from pytubefix.cli import on_progress
from yt_dlp import YoutubeDL

def safe_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '', name)

print('PASTE YOUTUBE URL HERE BETWEEN APOSTROPHE : ')
url = input()
print('TITLE OF THE SONG : ')
title = input()
print('ENTER ALBUM NAME : ')
albumName = input()
print('ENTER ARTIST ON THE TRACK : ')
artists = input()
print('ENTER ALBUM ARTIST')
albumArtist = input()
print('HOW MANY SONGS ARE IN THE ALBUM ? ')
totalTrack = input()
print('WHAT IS THE NUMBER OF THE TRACK YOU WANT TO DOWNLOAD ? ')
trackNum = input()
print('ENTER COVER ID (enter only the name, not the .jpg extension) IF NO ID, ENTER 0')
CoverID = input()

track_name = safe_filename(title)  

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
f['album'] = albumName
f['albumartist'] = albumArtist
f['artist'] = artists
f['totaltracks'] = totalTrack # IMPORTANT ENTER THE NUMBER OF SONG IN THE ALBUM.
f['tracknumber'] = trackNum # IMPORTANT ENTER THE NUMBER THAT THE TRACK HAS IN THE ALBUM.
if CoverID != '0':
    cover_path = '_cover\\'+ CoverID + '.jpg'
    with open(cover_path, 'rb') as img_in:
        f['artwork'] = img_in.read()
f.save()