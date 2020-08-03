var express = require('express');
var app = express();
var fs = require('fs');


Array.prototype.contains = function (obj) {
	var index = this.length;
	while (index--){
		 if (this[index] === obj){
			 return true;
		 }
	}
	return false;
}

var def_filter = {
	"band": ["ppp", "ro", "pp", "ag", "hhw", "ras", "mo", "other"],
	"diff": ["24", "25", "26", "27", "28"],
	"type": ["ex", "sp", "full"]
}
var other_band = ["rimi", "saaya", "arisa", "otae", "ayaxmocaxlisaxkanonxtsugu", "pppxykn", "ksmxranxayaxyknxkkr","hhwxranxaya", "roxran", "agxkkr", "pppxgg"];
app.all('*', function(req, res, next) {             //设置跨域访问
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.header("Access-Control-Allow-Methods", "GET");
    res.header("X-Powered-By", 'Bushiroad-NM$L');
    res.header("Content-Type", "application/json;charset=utf-8");
    next();
 });

app.get('/api',function(req,res){           //配置接口api
    res.status(200),
    diff_filter = req.query.diff;
    band_filter = req.query.band;
    type_filter = req.query.type;
    mode = req.query.mode;
    data_mode = req.query.data;
    
    result = {"msg": "error","result": []};
    if (!diff_filter){
		diff_filter = def_filter.diff;
	}else{
		diff_filter = diff_filter.split(',');
	}
    if (!band_filter){
		band_filter = def_filter.band;
	}else{
		band_filter = band_filter.split(',');
	}
    if (!type_filter){
		type_filter = def_filter.type;
	}else{
		type_filter = type_filter.split(',');
	}
	if(band_filter.contains("other")) {
		other_band.forEach(function(item){
			band_filter.push(item)
		});
	}
	if(data_mode == 'comp'){
		var song_data = require('./song_list_comp.json');
		console.log("load comp");
	}else{
		var song_data = require('./song_list.json');
		console.log("load normal");
	}
	
	
    fil_result = [];
    song_data.forEach(function(item,index){
		if (diff_filter.contains(item.diff) && band_filter.contains(item.band) && type_filter.contains(item.type)) {
			fil_result.push(item);
		}
	});
	if(fil_result == []){
		res.json(result);
		return;
	}
	if(mode == 'random'){
		result_song = [fil_result[Math.floor((Math.random()*fil_result.length))]];
	}else{
		result_song = fil_result
	}
	console.log(fil_result)
	result = {"msg": "ok","result": result_song};
    res.json(result);
})

//配置服务端口
var server = app.listen(3002,function(){
    var host = server.address().address;
    var port = server.address().port;
    console.log('listen at http://%s:%s',host,port);
})