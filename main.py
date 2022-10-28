from YtAudioScrapper import YouTubeScrapper
import os
import argparse
from rich.progress import track
from rich import print as rprint

# Path: detect.py

# yt = YouTubeScrapper()
# yt.get_video("Otha sollala")

if __name__ ==  "__main__" :
    parser = argparse.ArgumentParser(description= "Download youtube audio " )
    parser.add_argument( "-s" ,  "--songs" , help= "list of songs to download seperated with comma(,) add songs",required=True)
    parser.add_argument( "-o" ,  "--output" , help= "Output folder", required=False, default= "Music")
    args = parser.parse_args()
    yt = YouTubeScrapper(output_folder=args.output)
    for song in track(args.songs.split( "," ), description= "Downloading songs..." ):
    # for song in args.songs.split( "," ):
        yt.get_video(song)
    rprint( "Downloaded" , args.songs)
    # yt.get_video(args.songs)
    