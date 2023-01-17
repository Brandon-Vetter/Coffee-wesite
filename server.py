# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "172.29.223.172"
serverPort = 80

class Coffee(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        file = open("./" + self.path, "r")
        cont = file.read()
        self.wfile.write(bytes(cont, "utf-8"))
        file.close()
        self.end_headers()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), Coffee)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")