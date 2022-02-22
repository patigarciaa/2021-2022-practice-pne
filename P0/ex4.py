
import seq0
list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
FOLDER = "../Session04/"

for b in list_genes:
    filename = FOLDER + b
    f = seq0.seq_read_fasta(filename)
    counta, countc, countg, countt = seq0.count_bases(f)
    print("GEN", b)
    print("A:", counta, "\nC:", countc, "\nG:", countg, "\nT:", countt)