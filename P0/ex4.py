import seq0
list_genes = ["U5", "FRAT1", "ADA", "RNU6_269P", "FXN"]
d = count_bases(filename)
for l in list_genes:
    print("Gene", l, "\n", d)