#usar 127.0.0.1 o 0.0.0.0 como ip y el port el que sea for the server for client 127.0.0.1 es lo mas facil, 0.0.0.0 en client
#no funciona, pero tener 0.0.0.0 en server y 127.0.0.1 en client funciona
import socket
class client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("ok")


    def __str__(self): #queremos return la frasecita esta y printearla luego por otro lado
        return "Connection to SERVER at "+ self.ip + " PORT: " + str(self.port) #pongo sumas porque son todos
    # str y el unico que no es str que es interger, lo tranformo

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response

    def gen(self,msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        msg_2 = str.encode(msg)
        s.send(msg_2)
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response

