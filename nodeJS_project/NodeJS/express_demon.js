//express_demo.js 文件
var express = require('express');
var bodyParser = require('body-parser');
var pythonShell = require('python-shell');
var service_status = "1";
var options = {
	mode:'text',
  	pythonPath: "E:/Program Files/Python27/python.exe"
};
//var fork = require('child_process').fork;

var app = express();
var count = 0;


function updateTable(res){
	pythonShell.run('../../python_script/update_server.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  	    if (res){
  			res.send("1");
  		}
  		console.log('end: requet updateTable');
	});
}

function updateQuery(res){
 	pythonShell.run('../../python_script/update_query.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  		if (res){
  			res.send("1");
  		}
  		console.log('end: requet querytable');
	});
}

app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
  res.header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type");
  next();
});

app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
})); 

app.use(bodyParser.json());

app.get('/', function (req, res) {
	// var worker = fork('child_python.js')
	
	// worker.on('message',function(m){
	// 	worker.kill();
	// 	res.send(m);
	// });
	// worker.send('a');
	// count++;
 //    console.log('start'+count);

 //    pythonShell.run('js_python.py', options, function (err, results) {
 //  	if (err) throw err;
 //  	// results is an array consisting of messages collected during execution
 //  	res.send(results);
	// });
	// console.log('end'+count);

});

app.get('/fakequery',function (req, res) {
	// var worker = fork('child_python.js')
	
	// worker.on('message',function(m){
	// 	worker.kill();
	// 	res.send(m);
	// });
	// worker.send('a');

});

app.post('/fakequery',function (req, res) {
	// var worker = fork('child_python.js')
	
	// worker.on('message',function(m){
	// 	worker.kill();
	// 	res.send(m);
	// });
	// worker.send('a');
	console.log('start:query');
	options["args"] = [req.body["string"]];
    pythonShell.run('../../python_script/serverscript.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  		res.send(results);
  		console.log('end:query');
	});
});

app.post('/querycount',function (req, res) {
	// var worker = fork('child_python.js')
	
	// worker.on('message',function(m){
	// 	worker.kill();
	// 	res.send(m);
	// });
	// worker.send('a');
	console.log('request query count');
    pythonShell.run('../../python_script/get_query_count.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  		res.send(results);
  		console.log('end:request query count');
	});
});

app.post('/service_status',function (req, res) {
	console.log('request service_status');
	res.send(service_status);
	console.log('end:service_status');
});



app.post('/table_information',function (req, res) {
	console.log('request tableInformation');
    pythonShell.run('../../python_script/database_info.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  		res.send(results);
  		console.log('end:rquent tableInformation');
	});

});

app.post('/update_table',function (req, res) {
	console.log('request updateTable');
    updateTable(res);
});

app.post('/update_query',function (req, res) {
	console.log('request querytable');
   	updateQuery(res);
});


/*
* Here are some start shell command
*/
app.post('/restart_web_service',function (req, res) {
	console.log('request restart_web_service');
	res.send("0");
	console.log('end:restart_web_service');

});

app.post('/stop_web_service',function (req, res) {
	console.log('request stop_web_service');
	res.send("0");
	console.log('end:stop_web_service');

});


var server = app.listen(8081, 'localhost',function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log("应用实例，访问地址为 http://%s:%s", host, port);
});

