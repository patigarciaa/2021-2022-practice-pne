
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
        print("THERE WER SOME CONNECTION PROBLEMS, TRY AGAIN LATER")

#basic
data_list_species = request_server("/listSpecies?","limit=a&json=on")
termcolor.cprint("THE LIST IS:", "green")
print(data_list_species)


data_karyotype = request_server("/karyotype?", "species2=human&json=on")
termcolor.cprint("THE KARYOTYPE IS:", "green")
print(data_karyotype)

data_chromolength = request_server("/chromosomeLength?", "species3=human&chromosome=1&json=on")
termcolor.cprint("THE LENGTH IS:", "green")
print(data_chromolength)

#medium
data_seq = request_server("/geneSeq?", "gene_seq=FRAT1&json=on") #que pasa si mete un espacio
termcolor.cprint("THE SEQUENCE IS:", "green")
print(data_seq)

data_info = request_server("/geneInfo?", "gene_info=FRAT1&json=on")
termcolor.cprint("THE INFO IS:", "green")
print(data_info)


data_calc = request_server("/geneCalc?", "gene_calc=FRAT1&json=on")
termcolor.cprint("THE CALCULATIONS ARE:", "green")
print(data_calc)


data_list = request_server("/geneList?", "gene_list=9&start_limit=22125500&end_limit=22136000&json=on")
termcolor.cprint("THE LIST IS:", "green")
print(data_list)


