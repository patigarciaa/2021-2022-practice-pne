import socket
import termcolor
from seq1 import seq
import os
gen_list = ["ADA", "FRAT1", "U5", "FXN", "RNU6_269P"]


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
PORT = 8082
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
        split = msg.split("")
        command = split[0]

        if msg == "PING":
            termcolor.cprint("Ping command", "green")
            response = f"ok!"

        elif command == "GET":
            arg = int(split[1])
            gen = arg
            seq = seq()
            file = os.path.join(".", "gene_list", f"{gen}")
            seq.read_fasta(file)
            response = f"{seq}\n"
            cs.send(response.encode())

        elif command == "INFO":
            arg = split[1]
            sequence = seq(bases)
            response = f"{sequence.porcentages()}"

        elif command == "COMP":
            arg = split[1]
            sequence = seq(bases)
            response = f"{sequence.seq_complement()}"

        elif command == "GENE":
            arg = split[1]
            gen = gen_list[arg]
            seq = seq()
            file = os.path.join(".", "gene_list", f"{gen}")
            seq.read_fasta(file)
            response = f"{seq}\n"

        elif command == "REV":
            arg = split[1]
            sequence = seq(bases)
            response = f"{sequence.seq_reverse()}"

        cs.send(response.encode())
        cs.close() #cs es el client socket

except socket.error:
    print(f"problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("server stopped by the admin")
    ls.close() #ls es el socket del server
