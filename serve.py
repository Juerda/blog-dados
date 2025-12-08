#!/usr/bin/env python3
import os
import http.server
import socketserver
from pathlib import Path

os.chdir(Path(__file__).parent / 'output')

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        return super().end_headers()

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🚀 Servidor rodando em http://localhost:{PORT}")
    print(f"📁 Servindo arquivos de: {os.getcwd()}")
    print(f"🏠 Acesse: http://localhost:{PORT}/index.html")
    print()
    print("Pressione Ctrl+C para parar o servidor")
    httpd.serve_forever()
