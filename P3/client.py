
from client0 import client
gen_list = ["ADA", "FRAT1", "U5", "FXN", "RNU6_269P"]
seq_test = "ACGTACGT"

PRACTICE = 3

print(f"-----| Practice {PRACTICE} | -----")

IP = "127.0.0.1"
PORT = 8083
c = client(IP, PORT)
print(c)
c.debug("PING")
for i in range(5):
    c.debug(f"GET {i}")

c.debug(f"INFO {seq_test}")
c.debug(f"COMP {seq_test}")
c.debug(f"REV {seq_test}")
for i in gen_list:
    c.debug(f"GENE {i}")
c.debug(f"MULT {seq_test}")



