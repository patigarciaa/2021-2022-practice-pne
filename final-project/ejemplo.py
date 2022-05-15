import http
import json



SERVER = "rest.ensembl.org"
def request_ensembli(endpoint, params=""):
    conn = http.client.HTTPConnection(SERVER)
    parameters = "?content-type=application/json"
    try:
        conn.request("GET", SERVER + ENDPOINT + params + parameters)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    return json.loads(data1)

url = urlparse(self.path)
path = url.path
arguments = parse_qs(url.query)

if path == "/listspecies":
    n_species = arguments["number_species"][0]
    dict_answer = \request_ensembli("/info/species/", "el parametro que sea que en el basico de momento no lo voy a necesitar")
    list_species = dict_answer["species"]
    list_species = list_species[0:n_species]
    content = read_html_file("html/list_species.html")\.render(context={"species": list_species})