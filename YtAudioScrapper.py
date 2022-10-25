import os
import re
import urllib.request
from pytube import YouTube

# Python Class file for scrapping MP3

class YouTubeScrapper:

  def __init__(self, only_audio : bool = True, output_folder : str = "Music"):
    self.only_audio = only_audio
    self.output_folder = output_folder
    self.file_name = None

  def _song_name_preprcessor(self,song_name):
    return song_name.replace(" ","+")
    
  def get_video_link(self, song_name):
    print(f"Now Downloading ... {song_name}.mp3")
    song_name = self._song_name_preprcessor(song_name)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + song_name)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]
  
  def get_video(self,song_name):
    out_file = YouTube(self.get_video_link(song_name)).streams.filter(only_audio=True).first().download(os.getcwd() + '/' + self.output_folder)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    self.file_name = new_file
    return self.file_name

  def noise_removal(self):
    pass