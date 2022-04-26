

import http.server
import socketserver
import termcolor
import pathlib

# Define the Server's port
PORT = 8085

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""



        termcolor.cprint(self.requestline, 'green')
        route = self.requestline.split(" ")[1]

        if route == "/" or route == "mainpage.html":
            body = pathlib.Path("mainpage.html").read_text()
        else:
            try:
                filename = str(route) + ".html"
                body = pathlib.Path(filename.strip("/")).read_text()
            except FileNotFoundError:
                body = pathlib.Path("error.html").read_text()

        self.send_response(200)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(body.encode()))


        self.end_headers()


        self.wfile.write(body.encode())

        return


Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()