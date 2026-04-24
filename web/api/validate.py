from http.server import BaseHTTPRequestHandler
import json
import ast


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)

            files = data.get("files", {})
            results = {}

            for filename, code in files.items():
                if not filename.endswith(".py"):
                    continue
                try:
                    ast.parse(code)
                    results[filename] = {"valid": True}
                except SyntaxError as e:
                    results[filename] = {
                        "valid": False,
                        "error": str(e),
                        "line": e.lineno,
                        "offset": e.offset,
                        "text": e.text.strip() if e.text else None,
                    }

            all_valid = all(r["valid"] for r in results.values()) if results else True

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(
                json.dumps({"valid": all_valid, "results": results}).encode()
            )

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        pass
