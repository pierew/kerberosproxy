# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:08:42 2018

@author: PWoehl
"""

import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
kerberos_auth = HTTPKerberosAuth(mutual_authentication=REQUIRED, sanitize_mutual_error_response=False)
import argparse

URL = ""

class APIHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        r = requests.get(URL + self.path, auth=kerberos_auth, verify=False)
        self.wfile.write(r.text)

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers()
        r = requests.post(URL + self.path, auth=kerberos_auth, verify=False)
        self.wfile.write(r.text)
        
    def do_PATCH(self):
        self._set_headers()
        r = requests.patch(URL + self.path, auth=kerberos_auth, verify=False)
        self.wfile.write(r.text)
        
    def do_UPDATE(self):
        self._set_headers()
        r = requests.update(URL + self.path, auth=kerberos_auth, verify=False)
        self.wfile.write(r.text)
        
def run(server_class, handler_class, port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print "Starting httpd on", port
    httpd.serve_forever()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='HTTP/S Kerberos Gateway')
    parser.add_argument('--port', '-p', action="store", type=int, default=8080, help='port to listen on')
    parser.add_argument('redirect_url', action="store")

    arguments = parser.parse_args()
    
    URL = arguments.redirect_url
    port = arguments.port
    
    run(HTTPServer,APIHandler,port)
