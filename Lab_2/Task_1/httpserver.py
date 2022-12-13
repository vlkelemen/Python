from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
print('=== Start local webserver ===')
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
