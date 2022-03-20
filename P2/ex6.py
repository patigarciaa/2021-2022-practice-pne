from client0 import client
from seq1 import seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "localhost"
PORT = 8080
PORT2 = 8081
# -- Create a client object
c = client(IP, PORT)
c1 = client(IP, PORT2)

# -- Print the IP and PORTs
print(c)
print(c1)
gen = "FRAT1"
frag = 10
n_2 = 10
empty_seq = seq()
empty_seq.read_fasta(f".\sequences\{gen}")
print(f"Gen: {empty_seq}") #pongo empty_seq1 porque es realmente donde tengo el gen ya que la funcion me lo esta leyendo
c.talk(f"Sending gen {gen} to the server, in fragments of ten bases...")
number1 = 0
number2 = n_2
n_1 = 10
for b in range(1,n_1 + 1):#este range no me dice cuantas bases cjo si no cuantos grupos de 10 hago es decir 10 (1-11) y esto lo sabe por frag = empty...etc
    frag = empty_seq.bases[number1:number2] #bases va a ser las bases del gen si no pongo bases me va a dar null
    print(f"frag{b}: {frag}")
    number1 += n_2 #esto es para saltar de grupo en grupo
    number2 += n_2
    if b % 2 == 0:
        c1.talk(f"frag{b}: {frag}")
    else:
        c.talk(f"frag{b}: {frag}")




