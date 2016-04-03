//express_demo.js 文件
var express = require('express');
var bodyParser = require('body-parser');
var pythonShell = require('python-shell');
var options = {
	mode:'text',
  	pythonPath: "E:/Program Files/Python27/python.exe"
};
//var fork = require('child_process').fork;

var app = express();
var count = 0;
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

	console.log("run python shell"+ options);
    pythonShell.run('../../python_script/fake.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  		res.send(results);
  		console.log('end:query');
	});
});

var server = app.listen(8081, 'localhost',function () {

  var host = server.address().address
  var port = server.address().port

  console.log("应用实例，访问地址为 http://%s:%s", host, port)
});

