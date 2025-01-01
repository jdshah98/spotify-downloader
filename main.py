from __future__ import unicode_literals
from spotipy.oauth2 import *
import yt_dlp
import sys
import os

def download_video(url, out):
  os.system(f"yt-dlp --output {out} {url}")

def download_playlist(dir, input_file, output_filename):
  # create directory if not exists
  if not os.path.exists(dir):
    os.makedirs(dir)
  
  with open(input_file, "r") as inf:
    url_list = inf.read().splitlines()

    count=1
    for url in url_list:
      try:
        out_filepath = f"{dir}/{output_filename}_{count}"
        print(f"Downloading to {out_filepath}")
        download_video(url, out_filepath)
        print('download complete')
      except Exception as e:
        print(e)
      count+=1

if __name__ == "__main__":
  download_playlist(sys.argv[1], sys.argv[2], sys.argv[3])
