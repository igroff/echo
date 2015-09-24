#! /usr/bin/env python
from email.message import Message
import BaseHTTPServer
import logging
import json
import os

BaseHTTPServer.MessageClass = Message

class EchoHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def handle_request(self):
    resp_data = dict(clientAddress=self.client_address[0],
        method=self.command,
        uri=self.path,
        httpVersion=self.request_version,
        requestHeaders={key:self.headers[key] for key in self.headers.keys()}
    )
    self.send_response(200, '')
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(resp_data))

  def do_GET(self):
    self.handle_request()
    
  def do_POST(self):
    self.handle_request()

server = BaseHTTPServer.HTTPServer(('', int(os.environ.get('PORT', 8080))), EchoHandler)
server.serve_forever()
