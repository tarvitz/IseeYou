# -*- coding: utf-8
import re
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SocketServer
import simplejson as json
import db

PORT = 8930
HOST = ""

re_schema = re.compile('^/servers/$', re.M|re.U)

class B3BanServer(HTTPServer):
    def __init__(self, *args, **kwargs):
        super(B3BanServer, self).__init__(*args, **kwargs)

class B3BanRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # proceed get param
        if re.match(re_schema, self.path):
            self.send_response(200)
            self.send_header('Content-Type', 'text/javascript')
            self.end_headers()
            self.wfile.write(json.dumps(
                {'objects': db.get_servers()}
            ))
            return
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write('ok')
        return
        super(B3BanServer, self).do_GET()

    def do_POST(self):
        if re.match(re_schema, self.path):
            length = int(self.headers.getheader('Content-Length'))
            data = self.rfile.read(length)
            post = json.loads(data)
            db.add_server(**post)
            self.send_response(200)
            self.send_header("Content-Type", 'application/javascript')
            self.end_headers()
            self.wfile.write('"{success: true}"')
            return
        self.send_response(403)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write("POST not permitted here")
        return

    def do_DELETE(self):
        if re.match(re_schema, self.path):
            # duplicates, need cleanup
            length = int(self.headers.getheader('Content-Length'))
            data = self.rfile.read(length)
            post = json.loads(data)
            db.delete_server(**post)
            self.send_response(200)
            self.send_header("Content-Type", 'application/javascript')
            self.end_headers()
            self.wfile.write('"{success: true}"')
            return
        self.send_response(403)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write('DELETE not permitted here')
        return

    def do_PUT(self):
        if re.match(re_schema, self.path):
            # duplicates, need cleanup
            length = int(self.headers.getheader('Content-Length'))
            data = self.rfile.read(length)
            post = json.loads(data)
            db.update_server(**post)
            self.send_response(200)
            self.send_header("Content-Type", 'application/javascript')
            self.end_headers()
            self.wfile.write('"{success: true}"')
            return
        self.send_response(403)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write('DELETE not permitted here')
        return

Handler = B3BanRequestHandler

httpd = SocketServer.TCPServer((HOST, PORT), Handler)

print "serving at port", PORT
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print "Exiting"
    httpd.socket.close()
