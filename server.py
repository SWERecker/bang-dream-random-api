from flask import Flask, jsonify, request
import json
import random
app = Flask(__name__)

default_filter = {
    'band': ['ro', 'ppp', 'pp', 'ag', 'hhw', 'ras', 'mo', 'other'],
    'band_other': ['rimi', 'saaya', 'arisa', 'otae', 'ayaxmocaxlisaxkanonxtsugu', 'pppxykn', 'ksmxranxayaxyknxkkr',
                   'hhwxranxaya', 'roxran', 'agxkkr', 'pppxgg'],
    'diff': ['24', '25', '26', '27', '28', '29'],
    'type': ['ex', 'sp', 'full']
}

msg_error_band = {
    "msg": "error",
    "type": "band"
}
msg_error_diff = {
    "msg": "error",
    "type": "diff"
}
msg_error_type = {
    "msg": "error",
    "type": "type"
}
msg_error_result = {
    "msg": "error",
    "type": "result"
}


def random_song(band, diff, s_type, competitive=False):
    result = []
    song_filter = {
        'band': [],
        'diff': [],
        'type': []
    }
    if not band:
        song_filter['band'] = default_filter['band']
    else:
        song_filter['band'] = band
        for n in range(len(band)):
            if band[n] == 'other':
                del band[n]
                for name in default_filter['band_other']:
                    band.append(name)
    if not diff:
        song_filter['diff'] = default_filter['diff']
    else:
        song_filter['diff'] = diff
    if not s_type:
        song_filter['type'] = default_filter['type']
    else:
        song_filter['type'] = s_type

    if competitive:
        song_file = 'new_song_list_comp.json'
    else:
        song_file = 'new_song_list.json'
    print(song_filter)
    with open(song_file, 'r', encoding='utf-8') as song_file:
        dict_data = json.load(song_file)
        for i in range(len(dict_data)):
            if dict_data[i]['diff'] in song_filter['diff'] and \
                    dict_data[i]['band'] in song_filter['band'] and \
                    dict_data[i]['type'] in song_filter['type']:
                result.append(dict_data[i])
    if not result:
        return msg_error_result
    return json.dumps(random.choice(result), ensure_ascii=False)


@app.route('/random_song', methods=['post'])
def app_route():
    diff_filter = request.json.get('diff')
    band_filter = request.json.get('band')
    type_filter = request.json.get('type')
    if_competitive = request.json.get('c_type')
    return random_song(band_filter, diff_filter, type_filter, if_competitive)


app.run(host='0.0.0.0', port=8088, debug=True, threaded=True)
