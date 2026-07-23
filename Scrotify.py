import spotify_scraper as sc
from pytubefix.cli import on_progress
import os
from yt_dlp import YoutubeDL
import music_tag
import string
import random
from datetime import datetime
import re


class Album:
    def __init__(self, name, nb_tracks, artist, tracks, realeased, id):
        self.name = name
        self.nb_tracks = nb_tracks
        self.artist = artist
        self.tracks = tracks
        self.realeased = realeased
        self.id = id

    def getName(self):
        return self.name
    def getArtist(self):
        return self.artist[0]['name']
    def getTracks(self):
        return self.tracks
    def getRealeasedDate(self):
        return self.realeased
    def getNbTracks(self):
        return self.nb_tracks
    def getId(self):
        return self.id
    
    def __str__(self):
        return self.name
    
def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def safe_filename(name):

    name = re.sub(r'[<>:"/\\|?*\x00-\x1F]', ' ', name)
    name = re.sub(r'\s+', ' ', name)
    name = name.strip(' .')

    return name

# Enter if you have proxy adress
proxy = {
    "http": "socks5://proxy_address",
    "https": "socks5://proxy_address"
    }

# Initiate SpotifyClient for data

URL = [ # PASTE SPOTIFY ALBUM LINKS, NO LIMIT
    ]

for URLS in URL:

    client = sc.SpotifyClient()

    urls = [URLS]

    # Get album with all tracks
    album_list = []

    for i in urls:

        album = client.get_album_info(i)
        tracks = []
        for t in album['tracks']:
            tracks.append(t.get('name', 'Unknown'))
        a = Album(album.get('name','Unknown'), album.get('total_tracks', 0), album.get('artists', [{}]), tracks, album.get('realease_date', 'N/A'), id_generator())
        album_list.append(a)

        cover = client.download_cover(i, path='_cover\\', quality_preference='large', filename= a.getId() + '_cover')
        
    client.close()

    # Create spetial folder and PATH to download in respective folder (ALBUMNAME - ARTIST)
    PATH = []

    for alb in album_list:

        dir_name = safe_filename(alb.getName() + '-' + alb.getArtist())

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

    # Fetch for youtube link

    ytUrls = []
    MAX_RESULTS = 1

    opts = {
        "proxy": None,
        "default_search": "ytsearch",
        "noplaylist": True,
        "no_warnings": True,
        "extract_flat": True,
        "quiet": True
    }

    for albumm in album_list:

        #Verify that the list of every song that we fetch doesn't exceed the limit
        nbSongDDL = 0
        for i in album_list:
            nbSongDDL += i.getNbTracks()
        try:
            (nbSongDDL < 100) == True
        except:
            print('The number of song is too high for today lets go down a little')
        

        for tr in albumm.getTracks():
            print(tr)
            query = tr + ' ' + albumm.getArtist() 
            print(query)
            with YoutubeDL(opts) as yt:
                searchQuery = f"ytsearch{MAX_RESULTS}:{query}"
                info = yt.extract_info(searchQuery, download=False)
                entries = info.get('entries', [])
                # I think to ckeck if it's the right video, we need to check if Artists = Channel name ?
                for video in entries:
                    ytUrls.append(video.get("url"))
        
    print("\n")
    if (len(ytUrls) == album_list[0].getNbTracks()):
        print('--% Scroptify.exe - Downloader Status : Verified. ' + datetime.now().__str__() + ' : Operational for download.')
    else:
        print('ERROR FOUND : SCRAPING STEP FAILED % Some song will be missing, please correct them manually via DownloaderMan.py')
    print("\n")

    for k in ytUrls:
        print(k)

    # Downloads your freaking music, the last step to become independant dude

    i = 0
    for yt_urls in ytUrls:
        
        if len(ytUrls) == 0:
            break
        
        url = yt_urls
        track_name = safe_filename(album_list[0].getTracks()[i])
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
        print("Checking file:", pathfile)
        print("Exists:", os.path.exists(pathfile))
        print("Size:", os.path.getsize(pathfile) if os.path.exists(pathfile) else "N/A")

        # metadata editing
        f = music_tag.load_file(pathfile)
        f['title'] = album_list[0].getTracks()[i]
        f['album'] = album_list[0].getName()
        f['albumartist'] = album_list[0].getArtist()
        f['artist'] = album_list[0].getArtist()
        f['totaltracks'] = album_list[0].getNbTracks()
        f['tracknumber'] = i + 1
        cover_path = '_cover\\' + album_list[0].getId() + '_cover.jpg'
        with open(cover_path, 'rb') as img_in:
            f['artwork'] = img_in.read()
        f.save()
        i += 1
    print("\n")



        

