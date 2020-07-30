from flask import Flask, jsonify, request
import json
import random
app = Flask(__name__)


@app.route('/random_song', methods=['post'])
def get_ss():
    diff_fil_result = []
    band_fil_result = []
    type_fil_result = []

    diff_filter = request.json.get('diff')
    app.logger.info(diff_filter)
    band_filter = request.json.get('band')
    app.logger.info(band_filter)
    type_filter = request.json.get('type')
    app.logger.info(type_filter)
    song_type = request.json.get('c_type')

    if song_type == 'normal':
        song_file = 'new_song_list.json'
    else:
        song_file = 'new_song_list_comp.json'

    with open(song_file, 'r', encoding='utf-8') as song_file:
        dict_data = json.load(song_file)
        for i in range(len(dict_data)):
            if dict_data[i]['diff'] in diff_filter:
                diff_fil_result.append(dict_data[i])
        for i in range(len(dict_data)):
            if dict_data[i]['band'] in band_filter:
                band_fil_result.append(dict_data[i])
        for i in range(len(dict_data)):
            if dict_data[i]['type'] in type_filter:
                type_fil_result.append(dict_data[i])

        temp = [val for val in diff_fil_result if val in band_fil_result]
        result = [val for val in temp if val in type_fil_result]
        return jsonify(random.choice(result))


app.run(host='0.0.0.0', port=8802, debug=True)
