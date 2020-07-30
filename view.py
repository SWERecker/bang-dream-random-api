from flask import Flask, jsonify, request
import json
import random
app = Flask(__name__)


@app.route('/random_song', methods=['post'])
def get_ss():
    result = []
    diff_filter = request.json.get('diff')
    app.logger.info(diff_filter)
    band_filter = request.json.get('band')
    app.logger.info(band_filter)
    type_filter = request.json.get('type')
    app.logger.info(type_filter)
    song_type = request.json.get('c_type')

    if song_type == 'competitive':
        song_file = 'new_song_list_comp.json'
    else:
        song_file = 'new_song_list.json'

    with open(song_file, 'r', encoding='utf-8') as song_file:
        dict_data = json.load(song_file)
        for i in range(len(dict_data)):
            if dict_data[i]['diff'] in diff_filter \
                    and dict_data[i]['band'] in band_filter \
                    and dict_data[i]['type'] in type_filter:
                result.append(dict_data[i])
        if not result:
            return jsonify({"msg": "error"})
        random_song = random.choice(result)
        random_song["msg"] = "ok"
        return jsonify(random_song)


app.run(host='0.0.0.0', port=8802, debug=True, threaded=True)
