import http.server
import socketserver
import os

PORT = 8000

# Меняем текущую директорию на ту, где лежит этот скрипт (чтобы index.html точно находился)
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен. Перейдите по адресу:\n  http://localhost:{PORT}/index.html\n")
    httpd.serve_forever()
