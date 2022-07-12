from http.server import BaseHTTPRequestHandler
import socketserver

DISPLAY_TEXT = "Hello Tekton"

PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(DISPLAY_TEXT.encode())

with socketserver.TCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    print("Serving at port:", PORT)
    httpd.serve_forever()
