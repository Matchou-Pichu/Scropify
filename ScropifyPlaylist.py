import spotify_scraper as sc
from pytubefix.cli import on_progress
import os
from yt_dlp import YoutubeDL
import music_tag
import string
import random
from datetime import datetime
import re
    
def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def safe_filename(name):

    name = re.sub(r'[<>:"/\\|?*\x00-\x1F]', ' ', name)
    name = re.sub(r'\s+', ' ', name)
    name = name.strip(' .')

    return name

def get_tracks(plstTr):
    artist = []
    TrName = []
    for l in range(len(plstTr)):
        artist.append(safe_filename(plstTr[l]['artists'][0]['name']))
        TrName.append(safe_filename(plstTr[l]['name']))
    return artist, TrName

URL = [ # PASTE SPOTIFY ALBUM LINKS, NO LIMIT
    'https://open.spotify.com/playlist/6ReU9gwyYAdSxRlVQ80Hki?si=8bbnT3snS7OKaQ_fYK7c-w'
    ]

client = sc.SpotifyClient()

playlist = client.get_playlist_info('https://open.spotify.com/playlist/6ReU9gwyYAdSxRlVQ80Hki?si=8bbnT3snS7OKaQ_fYK7c-w')
playlist_list = [1]
nbTrack = len(playlist['tracks'])
playlistName = playlist['name']
PTracks = playlist['tracks']

# Create spetial folder and PATH to download in respective folder (PLAYLIST NAME | PLAYLIST)
PATH = []

for plt in playlist_list:

    dir_name = safe_filename(playlistName +  " - Playlist")

    # Creating directories for albums
    try:
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created successfully.\n\n")
        path = '.\\' + dir_name
        PATH.append(path)
    except FileExistsError:
        print(f"One or more directories in '{dir_name}' already exist.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{dir_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

MAX_RESULTS = 1
ytUrls = []

opts = {
        "proxy": None,
        "default_search": "ytsearch",
        "noplaylist": True,
        "no_warnings": True,
        "extract_flat": True,
        "quiet": True
    }

art, tr = get_tracks(PTracks)

for j in range(nbTrack):
        
    print(tr[j] + ' - ' + art[j])
    query = tr[j] + ' - ' + art[j]
    print(query)
    with YoutubeDL(opts) as yt:
        searchQuery = f"ytsearch{MAX_RESULTS}:{query}"
        info = yt.extract_info(searchQuery, download=False)
        entries = info.get('entries', [])
        # I think to ckeck if it's the right video, we need to check if Artists = Channel name ?
        for video in entries:
            ytUrls.append(video.get("url"))
        

if (len(ytUrls) == nbTrack):
    print('--% Scroptify.exe - Downloader Status : Verified. ' + datetime.now().__str__() + ' : Operational for download.')
else:
    print('ERROR FOUND : SCRAPING STEP FAILED % Some song will be missing, please correct them manually via DownloaderMan.py')
print("\n")

for k in ytUrls:
    print(k)

i = 0
for yt_urls in ytUrls:
    
    if len(ytUrls) == 0:
        break
    
    url = yt_urls
    track_name = safe_filename(tr[i])
    print('Track name : ' + track_name + '\n')
    output_template = os.path.join(PATH[0], track_name + ".%(ext)s")

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

    pathfile = PATH[0] + '\\' + track_name + '.m4a'
    print("Checking file: ", pathfile)
    print("Exists: ", os.path.exists(pathfile))
    print("Size: ", os.path.getsize(pathfile) if os.path.exists(pathfile) else "N/A")

    # metadata editing
    f = music_tag.load_file(pathfile)
    f['title'] = tr[i]
    f['albumartist'] = art[i]
    f['artist'] = art[i]
    f.save()
    i += 1
print("\n")


#[{'id': '', 'name': 'Ma trouve un solution', 'uri': 'spotify:track:0sVO7MPSMo8Qft12yPJ3g4', 'type': 'track', 'duration_ms': 282506, 'artists': [{'name': "Aim'a Nou", 'id': '', 'uri': '', 'type': 'artist'}]}