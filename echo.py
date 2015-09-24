#! /usr/bin/env python
import BaseHTTPServer
import logging
import json
from email.message import Message
import os


BaseHTTPServer.MessageClass = Message

class EchoHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def handle_request(self):
    resp_data = dict(clientAddress=self.client_address[0],
        method=self.command,
        uri=self.path,
        httpVersion=self.request_version,
        requestHeaders={}
    )
    for key in self.headers.keys():
        resp_data['requestHeaders'][key] = self.headers[key]
    
    self.send_response(200, '')
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(resp_data))

  def do_GET(self):
    logging.info("get")
    self.handle_request()
    
  def do_POST(self):
    logging.info("post")
    self.handle_request()

server = BaseHTTPServer.HTTPServer(('', int(os.environ.get('PORT', 8080))), EchoHandler)
server.serve_forever()
