import json

n = {
    "name": "*Re:birth day",
    "diff": "29",
    "band": "ro",
    "level": "ex",
    "type": "og"
}

#
with open('song_comp.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
# song_list = []
# l26 = []
#band_list = []
#for song in d:
#    band = song.get("band")
#    if band not in band_list:
#        band_list.append(song.get("band"))
#print(band_list)

with open('song_comp.json', 'w', encoding='utf-8') as f:
      f.write(json.dumps(d, ensure_ascii=False))
