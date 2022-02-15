def seq_ping():
    print("ok")


def valid_filename():
    exit = False
    while not exit:
        filename = input("What file do you want to open:")
        try:
            f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File does not exist. Provide another file")
def seq_read_fasta(filename):
    f = open(filename, "r").read()
    f = f[f.find("\n"):].replace("\n", "")
    return f

def count_bases(filename):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:  # assuming que el seq esta bien
        d[b] = d[b] + 1
    return d

