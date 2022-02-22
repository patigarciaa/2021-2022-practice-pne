def seq_ping():
    print("ok")


def valid_filename():
    exit = False
    while not exit:
        filename = input("What file do you want to open:")
        try:
            f = open("../session04/" + filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File does not exist. Provide another file")
def seq_read_fasta(filename):
    f = open(filename, "r").read()
    f = f[f.find("\n"):].replace("\n", "")
    return f

def count_bases(f):
    counta = 0
    countc = 0
    countg = 0
    countt = 0
    for l in f:
        if l == "A":
            counta += 1
        elif l == "C":
            countc += 1
        elif l == "G":
            countg += 1
        elif l == "T":
            countt += 1
    return counta, countc, countg, countt

def count_total_bases(f):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in f:
        d[b] += 1
    return d

def seq_reverse(f):
    new_seq = f[:20]
    new_seq = new_seq[::-1]
    return new_seq

def seq_complement(f):
    new_seq = f[:20]
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    return "".join([complement[base] for base in new_seq])

def biggest_base(f):
    bases = ["A", "C", "G", "T"]
    counta, countc, countg, countt = count_bases(f)
    counts = [counta, countc, countg, countt]
    zipped = zip(counts, bases)
    biggest = max(zipped)
    return biggest

