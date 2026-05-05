# Scropify V1

This is a cool tool that I coded to get rid of music subscription-based plateform. The goal is to migrate to a local way of listening music by taking all your album that you have on spotify and downloading it more easely 

## Get started

#### How to use Scropify ?

The main app is called Scropify and contains everything. First, copy as many album link as you'd like to download. Then, paste them in urls : 
```http
  URL = [ # PASTE SPOTIFY ALBUM LINKS, NO LIMIT
    'https://open.spotify.com/album/0eHXynBGM4KPnl8Mmv2xOY?si=-l8SGkVxSz6sRs6-pK6PJA'
    ]
```
It should have the 'https://open.spotify.com/album/' beginning in the urls. Make sure you paste it as a char, so that links can be used. Then you just need to run the code and voila.

#### ⚠ WARNING ⚠

The Scropify uses a method that DO NOT guarantee you a 100% accurate download efficiency. It means that you could have songs that does not correspond to the original songs from the album. For knowledge, it is a 95 % accuracy from what I experienced. Futher developpment will tackle this problem. For now, you should manually download the songs that are not correct by using ManualDownloaderMan.py. Search for the link on youtube, and paste it here :

```http
  url = 'PASTE YOUTUBE URLS HERE BETWEEN APOSTROPHE'
  track_name = safe_filename('TITLE OF THE SONG')  
```
You will have to change the metadata at the end of the file to have a good file management in whatever music app you are using. Here's some style that are annoying for the V1 :
| Style (typically the type of songs that are widely covered, with no )|    
| :-------- | 
| `Orchestra music` (everything that is classical, AAA movies soundtrack)      | 
| `Jazz music` |
| `Niche music` (exemple : Yaelokre, bulgarian folk music, etc...) |

