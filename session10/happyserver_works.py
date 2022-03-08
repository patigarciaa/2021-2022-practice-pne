import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "localhost"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# -- Waits for a client to connect
print("Waiting for Clients to connect")
ls.accept()

print("A client has connected to the server!")

# -- Close the socket
ls.close()
#como tengo el accept ya me wait for connections
#si pones un debug en el ultimo print no te va a dejar ir step by step porque esta esperado a que primero haya alguna conexion
#accept es un blocking function, aunque es verdad que si no le llega nada despues de un rato
#sigue runeando pero te saldra un error
#si me sale address already use, significa que estoy ya usando el port, tengo que parar el server1 para que el servr2 me funcione
#o con la funcion: #aparentemente lo pones al principio de todo
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
