# Scropify V2

This is a simple tool that I coded to slowly get music on the infamous subscription-based plateform Spotify. The goal is to migrate to a local way of listening music by taking all your album ad playlist that you have on spotify and downloading it more easely.

## Get started

#### How to install ?

For now, Scropify exists in a shell version, no executable version. You need to clone this project in order to use it. First of all, you need to install the latest version of Python that you can find on this page :

```http
https://www.python.org/downloads/windows/
```

After downloading and installing, search for Windows Powershell and check if it was correctly installed by searching for the version you installed (should return "Python 3.XX.X) :

```http
python --version
```

Congratulation, you installed python. Now, you need to install every librairy that the code needs to run. If you do not feel safe downloading those librairy, feel free to check every original git repo or website to check by yourself. Otherwise, install by copy/pasting the following code in WindowsPowershell:

```http
pip install spotifyscraper 
pip install pytubefix
pip install PyQt6
pip install yt-dlp
pip install music-tag
```
You are almost there ! Now that you downloaded each librairy, you need to download the project. To do so, go in the green section called code on top of the project and click Download Zip. De-compress the .zip fil and you are good to go ! Every time you want to use it, open your WindowsPowershell, and type these lines:

#### For Albums
```http
cd path/to/the/folder/containing/all/the/files
python ScropifyForAlbumGUI.py
```
#### For Playlist
```http
cd path/to/the/folder/containing/all/the/files
python ScropifyForPlaylistGUI.py
```
An interface should appear. Now it's time for you to download your saved album and playlist ! Enjoy freedom :).


#### ⚠ WARNING ⚠

The Scropify uses a method that DO NOT guarantee you a 100% accurate download efficiency. It means that you could have songs that does not correspond to the original songs from the album. For knowledge, it is a 95 % accuracy from what I experienced. Futher developpment will tackle this problem. For now, you should manually download the songs that are not correct by using ManualDownloaderMan.py. After pasting the following lines, follow the instructions:

```http
  cd path/to/the/folder/containing/all/the/files
  python ManualDownloaderMan.py
```
Here's some style that are annoying for the V2 :

| Style (typically the type of songs that are widely covered, with no )|    
| :-------- | 
| `Orchestra music` (everything that is classical, AAA movies soundtrack)      | 
| `Jazz music` |
| `Niche music` (exemple : Yaelokre, bulgarian folk music, etc...) |

