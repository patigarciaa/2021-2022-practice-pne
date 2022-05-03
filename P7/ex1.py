# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json


SERVER = 'rest.ensembl.org'
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
# se puede poner endpoint+ param o server+endpoint+param hay que probar ambas y ver que funciona

print(f"\nConnecting to server: {SERVER}\n")


# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT+PARAMS) #no hace falta poner el server en el url, solo neceistamos endpoint+ params

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server  #everything lo que esta de aqui para abajo es como si estuviese dentro del try, funcion igual
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
data2 = json.loads(data1)
if data2["ping"] == 1: #no poner ese 1 como string porque cuando usamos json mirar la explicacion de f:CONTENT, por eso aqui no
    #tranformamos nada a int, porque json ya lo hace por nosotros
    print("PING OK!! the database is running")
else:
    print("ERROR!! the database is not running")
# -- Print the received data
print(f"CONTENT: {data1}") #si ponemos aqui un type nos da que es interger porque el json crea un dictionary intenta convertir
#everything a su corresponding tipe en el caso del 1 un interger
#type error: string indeces must be interger significa que no he convertido mi string (que viene del json) a dictionary