#do_get(self):
    #-get url with urlparse
    #-get arguments with parse_qs

#-THE BIG IF
#example:
    #if path == "list_species":
        #SERVER = ""
        #ENDPOINT = ""
        #PARAMS = ""

        #HACER FUNCION Y METER DENTRO DE ESTA everything LO DE JSON ETC Y PONER RETURN DATA2 (EL DICT DE JASON) PONER EXCEPTIONES
        #A veces en el en los params puedes y debes mter varios params pones un & y añades el otro
        #poner como arg endpoint y params y añadir este param al PARAMS MEDIANTES UN +

import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from seq1 import seq
import json
import http.client

HTML_FOLDER = "./html/"
PORT = 8080
SERVER = 'rest.ensembl.org'

def request_ensembli(endpoint, params=""):
    conn = http.client.HTTPConnection(SERVER)

    #para el problema de los url con el json content type separado etc, se me ocurre crear un nuevo argumento
    #en la funcion, llamada parameters y dejar puesto en la funcion lo siguiente:
    #def request_ensembli(endpoint, parameters,params="")
    #always_parameters = "?content-type=application/json"
    #parameters_cal = parameters.split(=)
    #parameters_calc1 = parameters_calc[0]
    # parameters_calc2 = parameters_calc[1]
    #final parameter = parameters_calc1 + "=" + "text/plain"
    #luego en el elif pondria:
    #dict_answer = request_ensembli("endpoint"+ gene_cal, final_parameter, "")
    #y algo asi parecido con el otro

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
        # Message to send back to the client
        if self.path == "/":
            contents = read_html_file("index.html")\
                .render() #pasamos jinja a texto tal cual con el render

        elif path == "/listSpecies":
            limit = int(arguments["limit"][0])
            print("limit:", limit)
            dict_answer = request_ensembli("/info/species","")
            list_species = dict_answer["species"]
            longuitud = len(list_species)
            list_species2 = []
            for i in range(0,limit):
                list_species2.append(list_species[i]["common_name"])
            contents = read_html_file(path[1:] + ".html").render(context={"species": list_species2,
                                                                          "number": longuitud,
                                                                          "limit": limit})
            #con esto nos quitamos el / del /ping (nuestro path = endpoint)
            #y asi el programa entiende ping.html que es mi pagina html de ping abriendola

        elif path == "/karyotype":
            species2 = arguments["species2"][0] #me da human
            print("specie:", species2)
            print("type:", type(species2))
            dict_answer = request_ensembli("/info/assembly/"+ species2, "")
            print("dict:", dict_answer)
            list_karyo = dict_answer["karyotype"]
            print("list:", list_karyo)
            contents = read_html_file(path[1:] + ".html")\
                .render(context={"karyotype": list_karyo})
            #en este curso le damos un valor a una key, en vez de varios, por eso siempre es 0
            #VIP pasar a int porque si no luego en el siguiente paso no va a entender lo que le pido
             #pido la sequencia en la posicion_sequence que es un numero

        elif path == "/chromosomeLength":
            species3 = arguments["species3"][0]
            chromosome = arguments["chromosome"][0]
            dict_answer = request_ensembli("/info/assembly/" + species3, "")
            length = ""
            list_karyotype = dict_answer["karyotype"] #lista a secas
            print("list karyotype:", list_karyotype)
            list_all = dict_answer["top_level_region"] #lista de diccionarios
            print("list all:", list_all)
            for chromo in list_all:
                if chromo['name'] == chromosome:
                    length = chromo['length']
            print("chromo:", length)
            contents = read_html_file(path[1:] + ".html") \
                .render(context={"chromosome": length})

            #medium level
        elif path == "/geneSeq":
            gene_seq = arguments["gene_seq"][0]
            dict_answer = request_ensembli("/homology/symbol/human/"+ gene_seq, "") #la unica key que tiene es data
            info = dict_answer["data"] #info es un lista de diccionarios
            seq_dna = ""
            info2 = []
            for d in info:
                for dict in d["homologies"]:
                    info2.append(dict["source"])
                    for value in info2:
                        seq_dna = value["align_seq"]
            contents = read_html_file(path[1:] + ".html") \
                .render(context={"seq": seq_dna})

        elif path == "/geneInfo": #terminar
            gen_info = arguments["gen_info"][0]
            dict_answer = request_ensembli("/lookup/id/"+gen_info, "")
            print("dict:", dict_answer)
            contents = read_html_file(path[1:] + ".html") \
                .render(context={})


        elif path == "/geneCalc":
            gene_calc = arguments["gene_calc"][0]
            dict_answer = request_ensembli("/sequence/id/"+gene_calc, "")
            print("dict:", dict_answer)
            contents = read_html_file(path[1:] + ".html") \
                .render(context={})


        elif path == "/geneList":
            gene_list = arguments["gene_list"][0]
            start_limit = arguments["start_limit"][0]
            end_limit = arguments["end_limit"][0]
            endpoint1 = gene_list + ":" + start_limit + "-" + end_limit
            dict_answer = request_ensembli("/overlap/region/human/"+endpoint1, ";feature=gene;feature=transcript;feature=cds;feature=exon")
            print("dict:", dict_answer)
            contents = read_html_file(path[1:] + ".html") \
                .render(context={"gene": gene_list})

        else:
            contents = read_html_file("error.html") \
                .render()

        # Generating the response message
        self.send_response(200) # -- Status line: OK!

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

#en medium level hacer un while loop
