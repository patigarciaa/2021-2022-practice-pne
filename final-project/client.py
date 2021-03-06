
from client0 import client
import json
import http.client
import termcolor

PRACTICE = "FINAL PROJECT"

print(f"-----| Practice {PRACTICE} | -----")

SERVER = 'rest.ensembl.org'
IP = "127.0.0.1"
PORT = 8081
c = client(IP, PORT)
print(c)

def request_server(endpoint, params=""):
    try:
        conn = http.client.HTTPConnection(IP, PORT)
        try:
            conn.request("GET", endpoint+params)
        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()

        r1 = conn.getresponse()
        print(f"Response received!: {r1.status} {r1.reason}\n")
        if r1.status == 200:
            data1 = r1.read().decode("utf-8")
            data2 = json.loads(data1)
            return data2
        else:
            print("THERE WERE SOME CONNECTION PROBLEMS, TRY AGAIN LATER")
    except http.client.InvalidURL:
        print({"error": "THE URL COULD NOT BE FORMED, CHECK THE ENDPOINT AND PARAMS. THEY CAN NOT HAVE SPACES."})
    except json.decoder.JSONDecodeError:
        print({"error": "You did not include the json param, so you are asking for an html page, if you want to get the information, you should go to the browser."})

#basic
termcolor.cprint("THE LIST IS:", "green")
data_list_species = request_server("/listSpecies?","limit=10&json=1")
print(data_list_species)


termcolor.cprint("THE KARYOTYPE IS:", "green")
data_karyotype = request_server("/karyotype?", "species2=human&json=1")
print(data_karyotype)


termcolor.cprint("THE LENGTH IS:", "green")
data_chromolength = request_server("/chromosomeLength?", "species3=human&chromosome=1&json=1")
print(data_chromolength)



#medium
termcolor.cprint("THE SEQUENCE IS:", "green")
data_seq = request_server("/geneSeq?", "gene_seq=FRAT1&json=1") #que pasa si mete un espacio
print(data_seq)



termcolor.cprint("THE INFO IS:", "green")
data_info = request_server("/geneInfo?", "gene_info=FRAT1&json=1")
print(data_info)


termcolor.cprint("THE CALCULATIONS ARE:", "green")
data_calc = request_server("/geneCalc?", "gene_calc=FRAT1&json=1")
print(data_calc)


termcolor.cprint("THE LIST IS:", "green")
data_list = request_server("/geneList?", "gene_list=9&start_limit=22125500&end_limit=22136000&json=1")
print(data_list)


