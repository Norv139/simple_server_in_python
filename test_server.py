from http import server
import http
from http.server import HTTPServer, CGIHTTPRequestHandler, BaseHTTPRequestHandler

server = HTTPServer(('127.0.0.1', 8080), CGIHTTPRequestHandler)

server.serve_forever()

