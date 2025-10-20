from http.server import BaseHTTPRequestHandler, HTTPServer
import json




data = [
    {"id": 1, "name": "sam larry", "track": "AI Developer"},
    {"id": 2, "name": "Bolatito", "track": "AI Developer"}
]


class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status):
        self.send_response(status)
        self.send_header("center-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload, indent=2).encode())


    def do_POST(self, data):
        content_size = int(self.headers.get("content-length", 0))
        parsed_data = self.rfile.read(content_size)


        post_data = json.loads(parsed_data)
        print(post_data)
        post_data["id"] = len(data) + 1
        data.append(post_data)


        self.send_data({
            "message": "Data Received",
            "data": data
        }, status=201)


def run():
    HTTPServer(("localhost", 8000), BasicAPI).serve_forever()


print("running")
run()