# spotify-playlist-downloader
Simple python script to download tracks from spotify playlists, nothing fancy.

## Configuration
You need to obtain a spotify client id and client secret. You can do this by creating an app on the [spotify developer dashboard](https://developer.spotify.com/dashboard/applications). You can then set the client id and client secret in these lines:

```python
cid = "your client id"
secret = "your client secret"
```
Next, install the requirements by running 
```sh
pip3 install -r requirements.txt
```
You also need to install ffmpeg. You can do this by running `sudo apt install ffmpeg` on linux or by downloading it for any other OS from [here](https://ffmpeg.org/download.html).

## Usage
```sh
python3 spotify.py "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M" "music"
```
This will download the playlist and save it to the folder `music`. If the folder doesn't exist it will be created automatically.

## How it works
The script fetches the tracks list from the Spotify API using the playlist ID, searches for each audio on youtube using the track name and artist and downloads in 320kb/s bitrate and writes the audio metadata using [yt-dlp](https://github.com/yt-dlp/yt-dlp) and ffmpeg. 
```js
'preferredquality': '320', 
```
