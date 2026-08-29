import os
import json
import http.server
import socketserver

PORT = 8000
SCORES_FILE = "scores.json"

class ArcadeRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow cross-origin requests for safety
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        # Handle preflight CORS request
        self.send_response(200, "OK")
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/scores":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            # Load scores
            scores = self.load_scores()
            self.wfile.write(json.dumps(scores).encode("utf-8"))
        else:
            # Serve standard static files
            super().do_GET()

    def do_POST(self):
        if self.path == "/api/scores":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                new_score = json.loads(post_data.decode("utf-8"))
                scores = self.load_scores()
                
                # Insert and sort scores descending
                game = new_score.get("game", "Unknown")
                name = new_score.get("name", "Player")
                points = int(new_score.get("score", 0))
                
                if game not in scores:
                    scores[game] = []
                
                scores[game].append({"name": name, "score": points, "date": "Just Now"})
                # Sort and keep top 5
                scores[game] = sorted(scores[game], key=lambda x: x["score"], reverse=True)[:5]
                
                self.save_scores(scores)
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "scores": scores}).encode("utf-8"))
                
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f"Error parsing post data: {str(e)}".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def load_scores(self):
        if os.path.exists(SCORES_FILE):
            try:
                with open(SCORES_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                pass
        
        # Default scores if file does not exist
        return {
            "Snake": [
                {"name": "CYBER_BOY", "score": 250, "date": "2026-08-28"},
                {"name": "NET_RUNNER", "score": 180, "date": "2026-08-28"},
                {"name": "NEO", "score": 120, "date": "2026-08-28"}
            ],
            "SpaceDefenders": [
                {"name": "X_KILLER", "score": 3500, "date": "2026-08-28"},
                {"name": "ROBO_COP", "score": 2400, "date": "2026-08-28"},
                {"name": "NEO", "score": 1500, "date": "2026-08-28"}
            ],
            "BrickBreaker": [
                {"name": "PADDLE_MASTER", "score": 1200, "date": "2026-08-28"},
                {"name": "RETRO_FAN", "score": 900, "date": "2026-08-28"},
                {"name": "NEO", "score": 600, "date": "2026-08-28"}
            ]
        }

    def save_scores(self, scores):
        with open(SCORES_FILE, "w", encoding="utf-8") as f:
            json.dump(scores, f, indent=4)

def main():
    # Force working directory to directory containing this file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Enable socket re-use to avoid port conflicts
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), ArcadeRequestHandler) as httpd:
        print(f"Arcade Web Server started on http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            httpd.shutdown()

if __name__ == "__main__":
    main()
