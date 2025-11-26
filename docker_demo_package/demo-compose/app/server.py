
from http.server import BaseHTTPRequestHandler, HTTPServer
import redis, os

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(204)  # No Content
            self.end_headers()
            return
        count = r.incr("hits")
        msg = f"Hello from {os.getenv('SERVICE_NAME','web')} | hits={count}"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(msg.encode())

HTTPServer(("0.0.0.0", 8000), H).serve_forever()