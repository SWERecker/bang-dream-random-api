# 邦多利 随机选曲API

一个用Node.JS实现的随机选择BanG Dream!Girls Band Party中歌曲的API

默认端口3002，依赖express

### API参数列表
|参数名称|可接受的值|示例|说明|
|:--------:|-----|:----:|:----:|
|band|ppp, ro, ag, pp, hhw, ras, mo, other|ppp,ro|筛选乐队|
|diff|24~28|24,25,26|筛选难度|
|level|ex, sp, full|ex,sp|筛选歌曲类型|
|mode|random|random|是否随机一首歌|
|data|comp|comp|是否使用[第三方难度分级](#third)|
|type|og,co|co|og: 原创曲；co：翻唱曲|

* 所有参数间用**半角**逗号分隔
* 当不提供`mode=random`参数时，将会列出所有满足筛选条件的歌曲
* 选曲API收录了所有24~28难度的日服歌曲，数据为手工录入，可能有错误，可以发Issue指出

* 公共API：`http(s)://api.mocabot.cn/api` 支持HTTP(S)

### API请求示例

请求随机一首Poppin'Party或Hello, Happy World!的难度为26等级为SPECIAL的原创曲

`https://api.mocabot.cn/api?band=ppp,hhw&diff=26&mode=random&level=sp&type=og`

请求随机一首比赛曲库中难度为27的Roselia的歌曲

`https://api.mocabot.cn/api?band=ro&mode=random&data=comp`

请求随机一首SPECIAL等级的Pastel*Palettes的歌曲

`https://api.mocabot.cn/api?band=pp&level=sp&mode=random`

请求列出Roselia和Afterglow的难度为28的歌曲

`https://api.mocabot.cn/api?band=ro,ag&diff=28`

### API返回值
此API返回标准的JSON格式数据

当请求正确时，返回格式为：

    {
        "msg": "ok",
        "result": [
            {
                "name": "ときめきエクスペリエンス！", # 歌曲名称
                "band": "ppp", # 乐队简称
                "diff": "25", # 难度（String类型）
                "level": "ex", # 歌曲等级
                "type": "og" # 原创/翻唱曲
            },
            {
                "name": "Home Street", # 歌曲名称
                "band": "ppp", # 乐队简称
                "diff": "25", # 难度（String类型）
                "level": "ex", # 歌曲等级
                "type": "og" # 原创/翻唱曲
            }
            ...
        ]
    }

当请求错误时，（指筛选条件有误或者筛选条件下无歌曲的情况）：

	{
		"msg": "error",
		"result": []
	}
  
  
### 乐队 简称对应

    dictionary = {
        "band": {
            "ro": "Roselia",
            "ppp": "Poppin‘Party",
            "pp": "Pastel*Palettes",
            "ag": "Afterglow",
            "hhw": "Hello, Happy World",
            "ras": "RAISE A SUILEN",
            "mo": "Morfonica",
            "rimi": "牛込りみ",
            "saaya": "山吹沙綾",
            "arisa": "市ヶ谷有咲",
            "otae": "花園たえ",
            "ayaxmocaxlisaxkanonxtsugu": "彩×モカ×リサ×花音×つぐみ",
            "pppxykn": "Poppin‘Party×友希那",
            "ksmxranxayaxyknxkkr": "香澄×蘭×彩×友希那×こころ",
            "hhwxranxaya": "ハロハピ×蘭×彩",
            "roxran": "Roselia×蘭",
            "agxkkr": "Afterglow×こころ",
            "pppxgg": "Poppin‘Party × Glitter*Green"
        },
        "type": {
            "ex": "EXPERT",
            "sp": "SPECIAL",
            "full": "FULL"
        }
    }
  
### 第三方难度分级调整的难度<div id="third"></div>
  
  
|名称|类型|调整|
|  ----  | ----  | ---- |
|ときめきエクスペリエンス！|EXPERT|25 → 24|
|ドリームパレード|EXPERT|26 → 25|
|Redo|EXPERT|27 → 26|
|君じゃなきゃダメみたい|EXPERT|25 → 26|
|ハッピーシンセサイザ|EXPERT|26 → 27|
|ゴーカ！ごーかい！？ファントムシーフ！|EXPERT|27 → 28|
|わちゃ・もちゃ・ぺったん行進曲|EXPERT|26 → 25|
|SURVIVOR ねばーぎぶあっぷ！|SPECIAL|27 → 28|
|BLACK SHOUT|EXPERT|25 → 24|

|名称|类型|调整|
|  ----  | ----  | ---- |
|陽だまりロードナイト|EXPERT|25 → 25&26|
|GO! GO! MANIAC|EXPERT|26 → 26&27|
|Easy come easy go！|EXPERT|26 → 26&27|
|Paradisus-Paradoxum|EXPERT|28 → 27&28|
|God knows..|EXPERT|28 → 27&28|
|紅蓮の弓矢|EXPERT|27 → 26&27|
|天ノ弱|EXPERT|28 → 27&28|
|海色|EXPERT|26 → 26&27|
|Re:birth day|EXPERT|28 → 28&28+|
