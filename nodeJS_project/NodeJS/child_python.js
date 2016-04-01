var pythonShell = require('python-shell');
var options = {
  pythonPath: "E:/Program Files/Python27/python.exe"
};
process.on('message',function(m){
   	var pyshell = new pythonShell('js_python.py',options);
   	pyshell.end(function (err,results) {
  	if (err) throw err;
  	process.send("a");
  	console.log('finished');
	});

   	});

process.on('SIGHUP', function() {
        process.exit();//收到kill信息，进程退出
});