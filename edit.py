import json
to_del_list = []
with open('song_list.json', 'r', encoding='utf-8') as song_file:
	dict_data = json.load(song_file)
for index in range(len(dict_data)):
		dict_data[index]['id'] = index
		diff = int(dict_data[index].get('diff'))
		dict_data[index]['diff'] = diff


with open('new_song_list.json', 'w', encoding='utf-8') as new_song_file:
	new_song_file.write(json.dumps(dict_data, ensure_ascii=False, indent=4))