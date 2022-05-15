import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from seq1 import seq
HTML_FOLDER = "./html/"
LIST_SEQUENCES = ["ACGTCCAGTAAA", "ACGTAGTTTTTAAACCC", "GGGTAAACTACG",
                  "CGTAGTACGTA", "TGCATGCCGAT", "ATATATATATATATATATA"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU5A", "U5"]

def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents


def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1

    total = sum(d.values())
    for k,v in d.items():
        d[k] = [v, (v * 100) / total]
    return d


def convert_message(base_count): #lo convertimos a string para mandarlo al html
    message = ""
    for k,v in base_count.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)" +"<br>"
    return message

def info_operation(arg): #aqui el arg va a ser lo que pongamos despues en operation
    base_count = count_bases(arg)
    response = "<p> Sequence: " + arg + "</p>"
    response += "<p> Total length: " + str(len(arg)) + "</p>"
    response += convert_message(base_count)
    return response #todo esto es para ahorrar tiempo y poner los headers tal cual ya directamente

# Define the Server's port
PORT = 8086

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happytest server: It always returns a message saying
        # that everything is ok
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments", arguments)
        # Message to send back to the clinet
        if self.path == "/":
            contents = read_html_file("index.html")\
                .render(context=
                        {"n_sequences": len(LIST_SEQUENCES),
                         "genes": LIST_GENES}) #pasamos jinja (formato de json) a texto tal cual con el render

        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render() #con esto nos quitamos el / del /ping (nuestro path = endpoint)
            #y asi el programa entiende ping.html que es mi pagina html de ping abriendola

        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0]) #en este curso le damos un valor a una key, en vez de varios, por eso siempre es 0
            #VIP pasar a int porque si no luego en el siguiente paso no va a entender lo que le pido
            sequence = LIST_SEQUENCES[n_sequence] #pido la sequencia en la posicion_sequence que es un numero
            contents = read_html_file(path[1:] + ".html")\
                .render(context = {
                "n_sequence": n_sequence,
                "sequence": sequence
            }) #lo mismo de antes del render

        elif path == "/gene":
            gene_name = arguments["gene_name"][0]
            sequence = Path("./sequences/" + gene_name + ".txt").read_text()
            contents = read_html_file(path[1:] + ".html") \
                .render(context={
                "gene_name": gene_name,
                "sequence": sequence
            })

        elif path == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["operation"][0]
            s = seq(sequence) #pasamos por la funcion el sequence que viene a ser lo que va meter el usuario
            if operation == "rev":
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "operation": operation,
                    "result": s.seq_reverse()
                })
            elif operation == "info":
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "operation": operation,
                    "result": info_operation(sequence)
                })
            elif operation == "comp":
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "operation": operation,
                    "result": s.seq_complement()
                })
        else:
            contents = "I am the happy server! :-)"

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()