from client0 import client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 6123

# -- Create a client object
c = client(IP, PORT)

# -- Print the IP and PORTs
print(c)
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")

#bind hace que uno de los sockets sea pasivo y escuche (server) en el client no lo hacemos, para conectar client y server usamos .connect
#client NUNCA SE BIND # el port cambia porque estamos desde el client rendo distintos sockets
#el puerto que sle cuando esta conectando es uno especifico que se crea pero no el del client
# si me sale connecting 127.0.0.1 en puerto 8378 e intento conectar mi client poniendo ese puerto NO va funcionar
#por lo de puerto especifico etc..
#socket:abre un camino para conectar un ordenador con el otro
#defines el ip y port y lo binds en el server para que sea pasivo y reciba y escuche la informacion del client
#si usas un port entre 0-65535 va a funcionar siempre a no ser que sea linux que esta restringido a 0-1024
#usar  ip = 127.0.0.1 y port= 0.0.0.0 solo va a funcionar si el server y el client esta running en la misma mchine
#server.socket.listen(MAX_OPEN_REQUESTS) #max_open_request es una variable que tendra un numero asociado, este numero va a ser el max
#numero que el server puede atender. si no lo defines el mismo ordenador te dara un numero que desconoceremos.ç
#(clientsocket, address) = serversocket.accept() esto te vaa dar un socket especifico creado para la comunicacion entre clien1
#(por ejemplo) y el ip address del client1 (los returnea) esta funcion acepta las conexiones de fuera
#cuando vemos msg = clientsocket.no se que; ese socket es especifico del client esta funcion 
# #los verdaderos server siempre estan esperando conexiones aunque ya haya alguien conectado
