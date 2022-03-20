from seq1 import seq
list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
FOLDER = "../session04/"
for i in list_genes:
    filename = FOLDER + i
    from pathlib import Path
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    strbases = body
    for k, v in body.count_bases().items():
        print(k + ":", v)































