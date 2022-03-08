import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "localhost"#poner mi ip

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen() #si no especificas nada entre () elprograma will handle how many client en parallels

print("The server is configured!")

# -- Close the socket
ls.close()
#oseerror[Winerror 10048] = problema del ip
#si lo runeo sin accept function el server will finished