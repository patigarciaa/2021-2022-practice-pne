class seq: #los metodos no tienen por que return, cuando cambiamos atributos de la clase no hace falta return.
    """A class for representing sequences"""

    def __init__(self, bases="NULL"):
        self.bases = bases
        if bases == "NULL":
            print("Null sequence created")
            self.bases = "NULL"
        elif not self.valid_sequence():
            self.bases = "ERROR"
            print("ERROR!")
        else:
            self.bases = bases
            print("New sequence created!")

    def __str__(self):#funcion que me printea como str mi sequencia
        return self.bases

    def len(self): #metodo que cuenta
        return len(self.bases)
    def len_null_error(self):
        new_len = ""
        if seq == "NULL" or seq == "ERROR":
            len(new_len)
        return len(new_len)

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.bases) and valid:
            c = self.bases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def count_bases(self):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        try:
            for b in self.bases:  # assuming que el seq esta bien
                d[b] = d[b] + 1
        except KeyError:
            d =  {"A": 0, "C": 0, "G": 0, "T": 0}
        return d

    def seq_reverse(self):
        new_seq = []
        if self.bases == "ERROR" or self.bases == "NULL":
            new_seq = self.bases
        else:
            for i in self.bases:
                new_seq = self.bases[::-1]
        return new_seq

    def seq_complement(self):
        complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
        new_seq1 = ""
        if self.bases == "ERROR" or self.bases == "NULL":
            new_seq1 = self.bases
        else:
            for i in self.bases:
                new_seq1 += complement[i]
        return new_seq1

    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.bases = ""
        for lines in body:
            self.bases += lines


    def porcentages(self):
        porcentage = f"sequence: {self.bases}\n"
        porcentage += f"total length: {self.len()}\n"
        for k, v in self.count_bases().items():
            porcentage += f"{k}: {v} ({(v * 100) / self.len()}%)\n"
        return porcentage










