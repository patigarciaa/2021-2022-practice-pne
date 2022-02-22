import seq0
list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
FOLDER = "../Session04/"
for b in list_genes:
    filename = FOLDER + b
    f = seq0.seq_read_fasta(filename)
    d = seq0.count_bases(f)
    for k,v in seq0.count_total_bases(f).items():
        print("gen",b, "--->", k + ":", v)