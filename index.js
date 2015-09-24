var http = require('http');

var port = process.env.PORT || 3000;

var requestHandler = function(request, response){
  ret_object = {
    "headers": request.headers,
    "url": request.url,
    "method": request.method,
    "httpVersion": request.httpVersion,
  };
  // poor man's logging
  console.log(request.url);
  var body = '';
  request.on('data',  function(data){
    body += data.toString();
  });
  request.on('end', function(){
    ret_object.body = body;
    var response_string = JSON.stringify(ret_object);
    response.writeHead(200, {
      'Content-Length': Buffer.byteLength(response_string),
      'Content-Type': 'application/json',
      'Cache-Control': 'private',
      'Expires': 'Thu, 01 Dec 1999 16:00:00 GMT'
      });
    response.write(response_string);
    response.end();
  });
}
http.createServer(requestHandler).listen(port);
console.log('Listening on ' + port);
