import sys
import http.server
import socketserver

PORT = 8000

dir = None
if len(sys.argv) > 1:
    dir = sys.argv[1]
    print('Serving directory ', sys.argv[1])

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=dir, **kwargs)

handler = Handler
'''http.server.SimpleHTTPRequestHandler(directory=dir)'''
handler.extensions_map.update({
    '.wasm': 'application/wasm',
})

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.allow_reuse_address = True
    print("serving at port", PORT)
    httpd.serve_forever()
