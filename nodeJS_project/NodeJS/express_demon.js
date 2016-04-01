//express_demo.js 文件
var express = require('express');
var pythonShell = require('python-shell');
var options = {
	mode:'text',
  pythonPath: "E:/Program Files/Python27/python.exe"
};
//var fork = require('child_process').fork;

var app = express();
var count = 0;
app.get('/', function (req, res) {
	// var worker = fork('child_python.js')
	
	// worker.on('message',function(m){
	// 	worker.kill();
	// 	res.send(m);
	// });
	// worker.send('a');
	count++;
    console.log('start'+count);
    pythonShell.run('js_python.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  res.send(results);
});
	console.log('end'+count);

});

var server = app.listen(8081, 'localhost',function () {

  var host = server.address().address
  var port = server.address().port

  console.log("应用实例，访问地址为 http://%s:%s", host, port)
});