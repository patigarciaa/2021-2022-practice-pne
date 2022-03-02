import socket

# Configure the Server's IP and PORT
PORT = 6123
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept() #mi primer blocking sentences, el quote solo funcionara una vez pasado
        #esto, only one user can be connected at a time

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")#otro blocking sentence, hasta que no des un mensaje no sigue, y si
        #se mete otro al server no va a ir, el numero 2048 puede ser cualquier numero. utf-8 es un language coding podrias
        #quitarlo y seguiria funcionando, pero mejor dejarlo. El data que vamos a mandar va a ser bites, aunque
        #indirectamente podriamos enviar lo que queramos, dict, list etc.
        print("Message from client: {}".format(msg))

        # Send the messag
        message = "Hello from my server"
        send_bytes = str.encode(message) #lo pasamos a bites. Siempre que mandemos cosas distintas a strings, lo tenemos que pasar primero a str con la funcion str
        #no podemos pasar algo distinto de string a bytes
        # We must write bytes, not a string
        clientsocket.send(send_bytes)#lo mandamos
        clientsocket.close() #puede haber error si el user que esta dentro no cierra, ya que no puede conectarse mas de 1

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()