var app = require('express')();
var server = require('http').createServer(app);
var WebSocketServer = require('ws').Server;

app.get('/.test', function (req, res) {
  res.sendfile(__dirname + '/index.html');
});
app.get('/*', function(request, response) {
  console.log('auth', request.headers);
  response.end(request.path.slice(1));
});
var port = process.env.PORT || 3000;


server.listen(port);
var wsserver = new WebSocketServer({server: server});
wsserver.on('connection', function(socket){
  socket.on('message', function(data){
    console.log(data);
    socket.send(data);
  });
});


console.log('Listening on ' + port);
