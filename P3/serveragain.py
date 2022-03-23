import socket
import termcolor
from seq1 import seq
import os
gen_list = ["ADA", "FRAT1", "U5", "FXN", "RNU6_269P"]


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
PORT = 8083
IP = "127.0.0.1"
try:
    ls.bind((IP, PORT))
    ls.listen()
    print("The server is configured!")

    while True:
        print("Waiting for Clients to connect")
        (cs, client_ip_port) = ls.accept()
        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print(f"Message received: {msg}")
        response = ""

        split_msg = msg.split(" ")
        command_2 = split_msg[0]
        command = command_2.replace("\n", "").strip()#eliminar salto de linea y espacios del mensaje . replace y .strip
        termcolor.cprint(f"{command} command", "green")

        if command == "PING":
            response = f"ok!\n"

        elif command == "GET":
            arg = int(split_msg[1])
            gen = gen_list[arg]
            seq1 = seq() #llamar seq1 porque confunde la clase con la variable
            file = os.path.join(".", "sequences", f"{gen}")#para que entre a la folder etc para todos los sistems operativos
            seq1.read_fasta(file)
            response = f"{seq1}\n"


        elif command == "INFO":
            arg = split_msg[1]
            sequence = seq(arg)
            response = f"{sequence.porcentages()}"

        elif command == "COMP":
            arg = split_msg[1]
            sequence = seq(arg)
            response = f"{sequence.seq_complement()}"

        elif command == "GENE":
            arg = split_msg[1]
            seq1 = seq() #aqui lo mismo porque confunde la clase con la variable
            file = os.path.join(".", "sequences", f"{arg}")
            seq1.read_fasta(file)
            response = f"{seq1}\n"

        elif command == "REV":
            arg = split_msg[1]
            sequence = seq(arg)
            response = f"{sequence.seq_reverse()}"

        print(response)

        cs.send(response.encode())
        cs.close() #cs es el client socket

except socket.error:
    print(f"problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("server stopped by the admin")
    ls.close() #ls es el socket del server
