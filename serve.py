from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "contexto.politico" / "content"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(CONTENT_DIR), **kwargs)


if __name__ == "__main__":
    port = 8000
    with ThreadingHTTPServer(("127.0.0.1", port), Handler) as httpd:
        print(f"Sirviendo el portal en http://127.0.0.1:{port}")
        httpd.serve_forever()


