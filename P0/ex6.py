import seq0
b = "U5"
FOLDER = "../Session04/"
filename = FOLDER + b
f = seq0.seq_read_fasta(filename)
new_seq = seq0.seq_reverse(f)
print("Fragment U5 gene -->", f[:20])
print("Reverse U5 gene -->", new_seq)