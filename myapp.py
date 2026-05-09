from http.server import BaseHTTPRequestHandler, HTTPServer
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Docker Port Demo</title>
        <style>
        body{
            margin:0;
            font-family:Arial;
            background:linear-gradient(135deg,#667eea,#764ba2);
            color:white;
            text-align:center;
        }
        .container{
            margin-top:120px;
        }
        .card{
            background:white;
            color:black;
            width:500px;
            margin:auto;
            padding:40px;
            border-radius:12px;
            box-shadow:0 15px 40px rgba(0,0,0,0.3);
        }
        h1{
            color:#764ba2;
        }
        .port{
            font-size:20px;
            margin-top:20px;
            background:#f2f2f2;
            padding:10px;
            border-radius:6px;
        }
        footer{
            margin-top:40px;
            font-size:14px;
            opacity:0.8;
        }
        </style>
        </head>
        <body>
        <div class="container">
            <div class="card">
                <h1>🚀 Kubernetes Demo</h1>
                <p>This Python application is running inside a Kubernetes Pod.</p>
            </div>
            <footer>
            DevOps Kubernetes Demo
            </footer>
        </div>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())
server = HTTPServer(("0.0.0.0", 5000), MyHandler)
print("Server running on port 5000")
server.serve_forever()

