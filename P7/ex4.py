# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
from seq1 import seq
import json
genes_dict = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296","RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"}

gene_name = input("Enter a gene name please:")
for k, v in genes_dict.items():
    if gene_name == k:
        value = v



SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/" #change endpoint y other things
PARAMS = "?content-type=application/json"


print(f"\nConnecting to server: {SERVER}\n")

#rafael.villen.galera
# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT+value+PARAMS)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

except NameError:
    print("you have not enter a valid gene, try again")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
data2 = json.loads(data1) #data2 es toda mi info del mir



print("GENE:", gene_name)
for k, v in data2.items():
    if k == "seq":
        print("Bases:", v)
        s = seq(v)
        print("Number of bases:", s.count_bases())
        print("Number of bases", s.porcentages())
        print("Base most frequent:", s.most_common())
    elif k == "desc":
        print("Description:", v)


