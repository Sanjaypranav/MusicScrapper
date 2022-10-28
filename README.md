### To Run Scrapper file 
---
1. Install the requirements
2. Run the scrapper file
3. The output will be stored in the output folder

```bash
$ pip install -r requirements.txt
$ python3 detect.py -s "nakku mukka vj antony, mallipo"
```

or 

in ```scrapper.py``` file 

```python
list = [
    "List of songs along with artist name that you wan't to scrap!!"
]

yt = YouTubeScrapper(output_folder="Music")
for song in track(list, description="Downloading songs..."):
    yt.get_video(song)
```
then run

```bash
$ pip install -r requirements.txt
$ python3 scrapper.py
```