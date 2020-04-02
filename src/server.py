import http.server
import socketserver
import sys
import json

#---------------------------------------
# imports
import JaR_templating
import JaR_database_handling
import JaR_routing

PORT = 15400
    
class MySimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    mainDirectoryPath = "/home/jakovac/Desktop/Családi Cég/JaR-Project"

    def writeHeader(self, mimetype, response_code):
        self.send_response(response_code, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        if mimetype != "":
            self.send_header('Content-type', mimetype)
        #self.send_header("Content-Length", str(len('test1')) ) # <- NEM KELL
        self.end_headers()

    def do_OPTIONS(self):
        return

    def sendErrorResponse(self, error_code):
        self.writeHeader("text/html", error_code)
        self.wfile.write(
            JaR_templating.generateErrorHTML(error_code, self.mainDirectoryPath
                                             + "/templates/error.html")
        )
        

    # Problem: sends 403 error even if the request was only a typo
    def processInput(self):
        query_list = list(map(lambda x: x.strip(), self.path.split("?")))
        if len(query_list) == 1: #if there are no params: use empty params
            query_list.append("")
        query_list[0] = JaR_routing.getFilePathEnding(query_list[0]);
        print("PATH =", query_list[0])
        # security checking of the input html:
        allow = JaR_routing.isAllowed(query_list[0], self.mainDirectoryPath) 
        if allow[0] == False:
            self.sendErrorResponse(allow[1])
            # Error happened during the path analysis. Possible errors:
            # 403 - Forbidden (see https://kb.iu.edu/d/bfrc)
            # 404 - Page not found
            return # !!!!!
        
        path = self.mainDirectoryPath + query_list[0]
        
        params = {}
        if query_list[1] != "":
            params = dict(qc.split("=") for qc in query_list[1].split("&"))
            
        # params will be sent to handleFileRequest later...
        response = JaR_templating.handleFileRequest(path, params)
        if response[2] == 200:
            self.writeHeader( response[1], 200 ) # code 200 = OK
            self.wfile.write( response[0] )
        else: 
            # Error happened during the file templating. Possible errors:
            # 404 - Page not Found
            self.sendErrorResponse(response[2])
            
    def do_GET(self):
        #print("Asked for GET")
        self.processInput()
        
    def do_POST(self):
        #print("Asked for POST")
        self.processInput()
        

Handler = MySimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    sys.stderr.write("Starting server at port " + str(PORT) + "\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.stderr.write("Server Shutdown...\n")
        httpd.shutdown()
        httpd.server_close()
        
