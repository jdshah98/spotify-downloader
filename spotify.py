from __future__ import unicode_literals
import spotipy
from youtubesearchpython import VideosSearch
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import *
import json
import yt_dlp
import sys
import os
from video import Video
# from openpyxl import Workbook

# wb = Workbook()
# sheet = wb.active

cid = '' #CLIENT ID
secret = '' #CLIENT SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def call_playlist(creator, playlist_id):
    playlist_features_list = ["artist","album","track_name",  "track_id","danceability","energy","key","loudness","mode", "speechiness","instrumentalness","liveness","valence","tempo", "duration_ms","time_signature"]
   
    playlist = sp.user_playlist_tracks("spotify", playlist_id)["items"]
    track_df = []
    for track in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        
        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        track_df.append(playlist_features)
    return track_df

def download_audio(url, out):
    ydl_opts = {
        'format': 'bestaudio/best',
        'writethumbnail': True,
        'outtmpl': out,
        'postprocessors': [
          {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
          },
          {
            'key': 'FFmpegMetadata'
          },
          {
            'key': 'EmbedThumbnail'
          },
        ]
      }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])

def search(stuff):
  # search youtube for audio
  videos = VideosSearch(stuff)
  results = videos.result()['result']
  results = list(map(lambda v1: Video(v1), filter(lambda v2: Video(v2).validate(), results)))
  return results[0].link

def get_id(url): 
  # get playlist id from url
  return url.split("playlist/")[1].split("?")[0]

def create_query(audio): 
  # create query for youtube search
  return audio['track_name'] + ' ' + audio['artist'] + ' audio'

def download_playlist(url, dir):
  # create directory if not exists
  if not os.path.exists(dir):
    os.makedirs(dir)
  playlist = call_playlist('stuff', get_id(url))
  for audio in playlist:
    artist = audio['artist']
    track = audio['track_name']
    filename = f"{artist} - {track}.mp3"
    print(f"Downloading {filename}")
    try:
      download_audio(search(create_query(audio)), f"{dir}/{filename}")
      print('download complete')
    except Exception as e:
      print(e)

if __name__ == "__main__":
  download_playlist(sys.argv[1], sys.argv[2])
