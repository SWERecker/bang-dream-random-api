import requests
import json

url = 'http://127.0.0.1:8088/random_song'
dictionary = {
    'band': {
        'ro': 'Roselia',
        'ppp': 'Poppin‘Party',
        'pp': 'Pastel*Palettes',
        'ag': 'Afterglow',
        'hhw': 'Hello, Happy World',
        'ras': 'RAISE A SUILEN',
        'mo': 'Morfonica',
        'rimi': '牛込りみ',
        'saaya': '山吹沙綾',
        'arisa': '市ヶ谷有咲',
        'otae': 'GBP！スペシャルバンド',
        'ayaxmocaxlisaxkanonxtsugu': '彩×モカ×リサ×花音×つぐみ',
        'pppxykn': 'Poppin‘Party×友希那',
        'ksmxranxayaxyknxkkr': '香澄×蘭×彩×友希那×こころ',
        'hhwxranxaya': 'ハロハピ×蘭×彩',
        'roxran': 'Roselia×蘭',
        'agxkkr': 'Afterglow×こころ',
        'pppxgg': 'Poppin‘Party × Glitter*Green',
    },
    'type': {
        'ex': 'EXPERT',
        'sp': 'SPECIAL',
        'full': 'FULL'
    }
}


def rdm_song(text):
    l_text = text.lower().replace("；", ";").replace("，", ",").replace(" ", "")
    para = {}
    paras = l_text[4:].split(';')
    for t in paras:
        if t[:2] == '乐队':
            para["band"] = t[2:].split(',')
        if t[:2] == '难度':
            para["diff"] = t[2:].split(',')
        if t[:2] == '类型':
            para["type"] = t[2:].split(',')
        if t[:2] == '比赛':
            para["c_type"] = True
    print(para)
    r = requests.post(url, json=para)
    result = json.loads(r.text)
    result_name = result.get('name')
    result_band = dictionary['band'].get(result.get('band'))
    result_type = dictionary['type'].get(result.get('type'))
    result_diff = result.get('diff')
    if result.get("msg") == "error":
        if result.get("type") == "band":
            return "错误: 乐队条件错误\n支持: ppp, ro, ag, hhw, pp, other"
        if result.get("type") == "type":
            return "错误: 歌曲类型条件错误\n支持：ex, sp, full"
        if result.get("diff") == "type":
            return "错误: 难度条件错误\n支持：24~29"
    return "选歌结果：\n{} — {}\n{} {}".format(result_name, result_band, result_type, result_diff)