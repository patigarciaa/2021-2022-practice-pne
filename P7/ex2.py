
genes_dict = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296","RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"} #se buscan los ids en internet para todos los demass genes

print("DICTIONARY OF GENES")
print("WE HAVE:", len(genes_dict), "GENES")

for k, v in genes_dict.items():
    print(k, "--->", v)
