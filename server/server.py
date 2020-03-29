import http.server
import socketserver
import sys

import urllib.parse as urlparse


# -------------------------------------------------------------
# General part

import json

def getNode(nodeID):
    with open('main_graph.json') as json_file:
        data = json.load(json_file)
    return data[nodeID]

#node = getNode("mathematics")

#print(node)

#exit(0)

# -------------------------------------------------------------
# Web-specific part

PORT = 15400

mystr = b'Hello, world!'

    
class MySimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        #print("Asked for Options")
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        #self.send_header("Content-Length", str(len('test1')) )
        # <- NEM KELL
        self.end_headers()

    def getNodeFromUrlParams(self):
        query = urlparse.urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        return getNode(query_components["id"])

    def processInput(self):
        self.do_OPTIONS()
        try:
            node = self.getNodeFromUrlParams()
            self.wfile.write( bytes(str(node["children"]), encoding="utf-8") )
        except KeyError as err:
            sys.stderr.write("Request for unknown ID: " +
                             str(err.args[0]) + "\n")
    
    def do_GET(self):
        #print("Asked for GET")
        self.processInput()
        
    def do_POST(self):
        #print("Asked for POST")
        self.processInput()
        

Handler = MySimpleHTTPRequestHandler
#Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    sys.stderr.write("Starting server at port " + str(PORT) + "\n")
    try:
        httpd.serve_forever()
    except:
        sys.stderr.write("Server Shutdown...")
        httpd.shutdown()
        httpd.server_close()
        
