import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from seq1 import seq
import json
import http.client
import socket
import os

HTML_FOLDER = "./html/"
PORT = 8080
SERVER = 'rest.ensembl.org'
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP = "127.0.0.1"

try:
    ls.bind((IP, PORT))
    ls.listen()
    print("The server is configured!")

    while True:
        print("Waiting for Clients to connect")
        (cs, client_ip_port) = ls.accept()
        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        print(f"Message received: {msg}")
        response = ""

        split_msg = msg.split(" ")
        command_2 = split_msg[0]
        command = command_2.replace("\n", "").strip()#eliminar salto de linea y espacios del mensaje . replace y .strip
        termcolor.cprint(f"{command} command", "green")
except Exception as e:
    print(e)

except KeyboardInterrupt:
    print("server stopped by the admin")
    ls.close()  # ls es el socket del server


genes_dict = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296","RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"}

def request_ensembli(endpoint, params=""):
    conn = http.client.HTTPConnection(SERVER)
    #request_ensembli("/listSpecies", "&json=1")
    try:
        parameters = "?content-type=application/json"
        conn.request("GET",endpoint+parameters+params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data2 = json.loads(data1)
    return data2


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
        url_path = urlparse(self.path) #self.path existe en class TestHandler(http.server.BaseHTTPRequestHandler) va desde la primera
        #barra despues del puerto y server del url hasta el final. Urlparse te devuelve todos los trocitos en tupla del url
        path = url_path.path #con esto coges la tupla que te ha dado el urlparse y le dices que quieres solo el path
        #es decir el endpoint
        print("QUERY:", url_path.query)#es un string
        arguments = parse_qs(url_path.query) #url_path.query te da  desde la ? hasta el final en forma de string,
        # parse_qs devuelve diccionario con keys y los values
        #puestos en una list, en nuestro caso la lista solo tiene 1 elemento siempre, por eso ponemos la posicion 0 siempre
        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments", arguments)


        ls.bind((IP, PORT))
        ls.listen()
        print("The server is configured!")


        print("Waiting for Clients to connect")
        (cs, client_ip_port) = ls.accept()
        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        print(f"Message received: {msg}")
        response = ""

        split_msg = msg.split(" ")
        command_2 = split_msg[0]
        command = command_2.replace("\n","").strip()  # eliminar salto de linea y espacios del mensaje . replace y .strip
        termcolor.cprint(f"{command} command", "green")

        # Message to send back to the client
        if self.path == "/":
            contents = read_html_file("index.html")\
                .render() #pasamos jinja a texto tal cual con el render

        elif path == "/listSpecies":
            try:
                limit = int(arguments["limit"][0])
                print("limit:", limit)
                dict_answer = request_ensembli("/info/species","")
                list_species = dict_answer["species"]
                longuitud = len(list_species)
                list_species2 = []
                if limit > int(longuitud):
                    message = "Sorry You chose a very high number it should be between 1-311"
                else:
                    message = ""
                    for i in range(0,limit):
                        list_species2.append(list_species[i]["common_name"])
                if "json" in arguments:
                    contents = {"species": list_species2,
                                "number": longuitud,
                                "limit": limit}

                elif command == "listSpecies":
                    contents = {"species": list_species2,
                                "number": longuitud,
                                "limit": limit}
                    response = f"{contents}\n"
                else:
                    contents = read_html_file(path[1:] + ".html").render(context={"species": list_species2,
                                "number": longuitud,
                                "limit": limit, "message": message})
            except ValueError:
                contents = read_html_file("error.html") \
                    .render()
            #con esto nos quitamos el / del /ping (nuestro path = endpoint)
            #y asi el programa entiende ping.html que es mi pagina html de ping abriendola


        elif path == "/karyotype":
            try:
                species2 = arguments["species2"][0] #me da human
                dict_answer = request_ensembli("/info/assembly/"+ species2, "")
                list_karyo = dict_answer["karyotype"]
                if "json" in arguments:
                    contents = {"karyotype": list_karyo}
                else:
                    contents = read_html_file(path[1:] + ".html")\
                        .render(context={"karyotype": list_karyo})
            except KeyError:
                contents = read_html_file("error.html") \
                    .render()

            #en este curso le damos un valor a una key, en vez de varios, por eso siempre es 0
            #VIP pasar a int porque si no luego en el siguiente paso no va a entender lo que le pido
             #pido la sequencia en la posicion_sequence que es un numero

        elif path == "/chromosomeLength":
            try:
                species3 = arguments["species3"][0]
                chromosome = arguments["chromosome"][0]
                dict_answer = request_ensembli("/info/assembly/" + species3, "")
                length = ""
                try:
                    level_region = dict_answer["top_level_region"] #lista a secas
                    for d in level_region:
                        if d['coord_system'] == "chromosome" and d["name"] == chromosome:
                            length += str(d['length'])
                    if "json" in arguments:
                        contents = {"chromosome": length}
                    else:
                        contents = read_html_file(path[1:] + ".html") \
                            .render(context={"chromosome": length})
                except KeyError:
                        contents = read_html_file("error.html") \
                        .render()
            except KeyError:
                contents = read_html_file("error.html") \
                    .render()



            #medium level
        elif path == "/geneSeq":
            try:
                gene_seq = arguments["gene_seq"][0] #esto va  ser tipo FRAT1
                stable_id = genes_dict[gene_seq]
                dict_answer = request_ensembli("/sequence/id/"+ stable_id, "")
                info = dict_answer["seq"]
                if "json" in arguments:
                    contents = {"seq": info}
                else:
                    contents = read_html_file(path[1:] + ".html") \
                        .render(context={"seq": info})
            except KeyError:
                contents = read_html_file("error.html") \
                    .render()



        elif path == "/geneInfo": #terminar
            try:
                gene_info = arguments["gene_info"][0] #va a ser FRAT1
                stable_id = genes_dict[gene_info]
                dict_answer = request_ensembli("/sequence/id/"+stable_id, "")
                info = dict_answer["desc"]
                split_info = info.split(":")
                gene_start = int(split_info[3])
                gene_end = int(split_info[4])
                length = gene_end - gene_start
                if "json" in arguments:
                    contents = {"start": gene_start, "end": gene_end, "length":length, "name": gene_info, "id": stable_id}
                else:
                    contents = read_html_file(path[1:] + ".html") \
                        .render(context={"start": gene_start, "end": gene_end ,  "length":length, "name": gene_info,"id": stable_id})
            except KeyError:
                contents = read_html_file("error.html") \
                    .render()


        elif path == "/geneCalc":
            try:
                gene_calc = arguments["gene_calc"][0]
                stable_id = genes_dict[gene_calc]
                dict_answer = request_ensembli("/sequence/id/"+stable_id, "")
                seq_given = dict_answer["seq"]
                s = seq(seq_given)
                print("dict:", dict_answer)
                if "json" in arguments:
                    contents = {"length": s.len(), "bases": count_bases(seq_given), "seq": gene_calc}
                else:
                    contents = read_html_file(path[1:] + ".html") \
                        .render(context={"length": s.len(), "bases": count_bases(seq_given), "seq": gene_calc})
            except KeyError:
                contents = read_html_file("error.html") \
                    .render()


        elif path == "/geneList":
            try:
                gene_list = arguments["gene_list"][0] #el chromo que quiero
                start_limit = arguments["start_limit"][0] #donde empiezo
                end_limit = arguments["end_limit"][0] #donde acabo
                endpoint2 = gene_list + ":" + start_limit + "-" + end_limit
                dict_answer = request_ensembli("/phenotype/region/homo_sapiens/"+endpoint2, ";feature_type=Variation")
                list_genes = []
                try:
                    for d in dict_answer:
                        for dict in d["phenotype_associations"]:
                            if "attributes" in dict:
                                if "associated_gene" in dict["attributes"]:
                                    list_genes.append(dict["attributes"]["associated_gene"])
                    print("list:", list_genes)
                    if "json" in arguments:
                        contents = {"gene": list_genes}
                    else:
                        contents = read_html_file(path[1:] + ".html").render(context={"gene": list_genes})
                except TypeError:
                    contents = read_html_file("error.html") \
                        .render()
            except KeyError:
                contents = read_html_file("error.html") \
                    .render()

        else:
            contents = read_html_file("error.html") \
                .render()

        # Generating the response message
        self.send_response(200) # -- Status line: OK!

        # Define the content-type header:
        #if "json" in arguments.keys() -> contents = json.dumps(context), content_type = application/json
        #else content_type = "text/html"

        print(response)

        cs.send(response.encode())
        cs.close()  # cs es el client socket

        if "json" in arguments.keys():
            contents = json.dumps(contents)
            self.send_header('Content-Type', 'application/json')
        else:
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

#en medium level hacer un while loop
