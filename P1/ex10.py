from seq1 import seq
list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
FOLDER = "./sequences/"
for i in list_genes:
    filename = FOLDER + i
    seq1 = seq()
    seq1.read_fasta(filename)
    frequent = None
    for k, v in seq1.count_bases().items():
        if frequent:
            if v > frequent[1]:
                frequent = (k, v)
        else:
            frequent = (k, v)
    print(f"Most frequent base in {i} is: {frequent}")


































