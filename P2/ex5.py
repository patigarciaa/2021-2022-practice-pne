from client0 import client
from seq1 import seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "localhost"
PORT = 8080

# -- Create a client object
c = client(IP, PORT)

# -- Print the IP and PORTs
print(c)

gen = "FRAT1"
n_1 = 5 #
n_2 = 10
empty_seq1 = seq()
empty_seq1.read_fasta(f".\sequences\{gen}")
c.talk(f"sending {gen} to the server, in fragment of ten bases...")
number1 = 0 #donde empezamos a leer nuestros fragments
number2 = n_2 #es igual a 10 porque es donde acaba de leer el primer fragmento
for b in range(1,n_1 + 1):#este range no me dice cuantas bases cjo si no cuantos grupos de 10 hago es decir 5 (1-6) y esto lo sabe por frag = empty...etc
    frag = empty_seq1.bases[number1:number2] #bases va a ser las bases del gen si no pongo bases me va a dar null
    print(f"frag{b}: {frag}")
    c.talk(frag)
    number1 += n_2 #esto es para saltar de grupo en grupo
    number2 += n_2