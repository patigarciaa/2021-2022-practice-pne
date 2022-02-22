import seq0
b = "U5"
FOLDER = "../Session04/"
filename = FOLDER + b
f = seq0.seq_read_fasta(filename)
print("fragment U5 gene -->", f[:20])
print("complement U5 gene -->", seq0.seq_complement(f[:20]))