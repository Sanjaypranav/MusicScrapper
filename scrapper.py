from YtAudioScrapper import YouTubeScrapper
import os
from rich.progress import track
from rich import print as rprint

list = [
    "chillax vijay antony",
    "pottu thakku",
    "manmadha rasa Danush",
    "macha meesa",
    "padichu pathen danush",
    "seena thaana",
    "Madura kulunga",
    "Asai Dosa Ajith",
    "Thirunelveli Halwada",
    "Dindukkallu Dindukkallu", #kuthu songs tamil recommended by github copilot
    "Sonna Puriyathu vijay",
    "Malayaru Remix DJ",
    "Kathala Kannala",
    "Thayya Thayya uyire"
]

yt = YouTubeScrapper(output_folder="Music")
for song in track(list, description="Downloading songs..."):
    yt.get_video(song)