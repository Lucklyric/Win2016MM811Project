//express_demo.js 
var express = require('express');
var bodyParser = require('body-parser');
var pythonShell = require('python-shell');
var exec = require('child_process').exec;
var web_service_status = 1;
var app_service_status = 0;
var options = {
	mode:'text'
};
//var fork = require('child_process').fork;

var app = express();
var count = 0;

//call correspoindg python scripts
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

function check_app_service_status(res){
	if (app_service_status == 1){
		return true;
	}else{
		res.send('3');
		return false;
	}
}

//initilize some parameters
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

});

app.get('/fakequery',function (req, res) {

});

// query request
app.post('/fakequery',function (req, res) {
	// var worker = fork('child_python.js')
	
	// worker.on('message',function(m){
	// 	worker.kill();
	// 	res.send(m);
	// });
	// worker.send('a');

	// check the status of the app service
	if (app_service_status == 1){
		
	}else{
		res.send('3');
		return;
	}
	console.log('start:query');
	options["args"] = [req.body["string"]];
    pythonShell.run('../../python_script/serverscript.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  		res.send(results);
  		console.log('end:query');
	});
});

// return the query counts information
app.post('/querycount',function (req, res) {

	console.log('request query count');
    pythonShell.run('../../python_script/get_query_count.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  		res.send(results);
  		console.log('end:request query count');
	});
});

//return the web service status
app.post('/service_status',function (req, res) {

	console.log('request service_status');
	res.send(web_service_status.toString());
	console.log('end:service_status');
});

//return the app service status
app.post('/app_service_status',function (req, res) {

	console.log('request service_status');
	res.send(app_service_status.toString());
	console.log('end:service_status');
});

// requert the table information
app.post('/table_information',function (req, res) {

	console.log('request tableInformation');
    pythonShell.run('../../python_script/database_info.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  		res.send(results);
  		console.log('end:rquent tableInformation');
	});

});

//update the public table
app.post('/update_table',function (req, res) {

	console.log('request updateTable');
    updateTable(res);
});

// update the user query table
app.post('/update_query',function (req, res) {

	console.log('request querytable');
   	updateQuery(res);

});

//stop app service
app.post('/stop_app_server',function (req, res) {

	console.log('request stop_app_server');
	app_service_status = 0;
	res.send("2");
	console.log('request stop_app_server');

});

// start app service
app.post('/start_app_server',function (req, res) {

	console.log('request start_app_server');
	app_service_status = 1;
	res.send("1");
	console.log('request stop_app_server');

});


/*
* Here are some start shell command
*/
app.post('/restart_web_service',function (req, res) {
	console.log('request restart_web_service');
	
	exec("/opt/lampp/xampp restart", function(error, stdout, stderr) {
  // command output is in stdout
  		console.log(stdout);
  		res.send("1");
  		console.log('end:restart_web_service');
	});
	
});

//Stop web server
app.post('/stop_web_service',function (req, res) {
	console.log('request stop_web_service');
	res.send("1");
	console.log('end:stop_web_service');

});

// Start the server
var server = app.listen(8081,function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log("App server http://%s:%s", host, port);
});

