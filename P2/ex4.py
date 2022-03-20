from client0 import client
from seq1 import seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "localhost"
PORT = 8080

# -- Create a client object
c = client(IP, PORT)

# -- Print the IP and PORTs
print(c)

list_genes = ["U5", "ADA", "FRAT1"]
for b in list_genes:
    empty_seq = seq()
    empty_seq.read_fasta(f".\sequences\{b}")
    c.talk(f"sending {b} to the server")
    c.talk(str(empty_seq)) #porque lo tenia en bytes y lo quiero en str


