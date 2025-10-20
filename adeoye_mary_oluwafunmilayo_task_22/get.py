from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {"id": 1, "name": "sam larry",
     "track": "AI Developer"},
     {"id": 2, "name": "Bolatito",
      "track": "AI Develop"}
]


class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status):
        self.send_response(status)
        self.send_header("content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload, indent=2).encode())
        

    def do_GET(self):
        self.send_data(data, 200)
            
def run():
    HTTPServer(("localhost", 8000), BasicAPI).serve_forever()




print("running")

run()

