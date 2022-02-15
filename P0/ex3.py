
import seq0
list_genes = ["U5", "FRAT1", "ADA", "RNU6_269P", "FXN"]
for l in list_genes:
    print("Gene", l, "---> Length", len(seq0.seq_read_fasta("../session04/" + l)))
    #get sequence
    #count bases with sequence
