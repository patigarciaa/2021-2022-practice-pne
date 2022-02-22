import seq0
list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
FOLDER = "../Session04/"
for b in list_genes:
    filename = FOLDER + b
    f = seq0.seq_read_fasta(filename)
    biggest = seq0.biggest_base(f)
    print("gen", b,":", "most frequent base -->", biggest[1])