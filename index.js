var http = require('http');

var port = process.env.PORT || 3000;

var requestHandler = function(request, response){
  ret_object = {
    "headers": request.headers,
    "url": request.url,
    "method": request.method,
    "httpVersion": request.httpVersion,
  };
  var body = '';
  request.on('data',  function(data){
    body += data.toString();
  });
  request.on('end', function(){
    ret_object.body = body;
    var response_string = JSON.stringify(ret_object);
    response.writeHead(200, {
      'Content-Length': response_string.length,
      'Content-Type': 'application/json',
      'Cache-Control': 'public'
      });
    response.write(response_string);
    response.end();
  });
}
http.createServer(requestHandler).listen(port);
console.log('Listening on ' + port);
