import socket
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        sz = int(self.headers['Content-Length'])
        dat = self.rfile.read(sz)
        print(dat)
        self.send_response(200)
    def do_GET(self):
        self.wfile.write(b"<html><head><script>alert('hi!!')</script></head></html>")
        self.send_response(200)


serv = HTTPServer(("0.0.0.0", 8080), Handler)
try:
    serv.serve_forever()
except KeyboardInterrupt:
    pass

print("Server exited cleanly.")
