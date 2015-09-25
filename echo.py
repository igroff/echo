#! /usr/bin/env python
from email.message import Message
import BaseHTTPServer
import logging
import json
import os

BaseHTTPServer.MessageClass = Message

class EchoHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    # a method for handling our any requests given, simply echo's back
    # the content of the request including any headers as a json object
    def handle_request(self):
        resp_data = dict(clientAddress=self.client_address[0],
            method=self.command,
            uri=self.path,
            httpVersion=self.request_version,
            requestHeaders={key:self.headers[key] for key in self.headers.keys()}
        )
        # everything is always good
        self.send_response(200, '')
        # we'll be returning json
        self.send_header('Content-Type', 'application/json')
        request_length = int(resp_data['requestHeaders'].get('content-length', 0))
        if request_length:
            resp_data['body'] = self.rfile.read(request_length)
        self.wfile.write("\n\n%s" % json.dumps(resp_data))

    def __getattr__(self, name):
        if "do_" == name[0:3]:
            return self.handle_request
    

server = BaseHTTPServer.HTTPServer(('', int(os.environ.get('PORT', 8080))), EchoHandler)
server.serve_forever()
