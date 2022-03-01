class seq: #los metodos no tienen por que return, cuando cambiamos atributos de la clase no hace falta return.
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            print("Null sequence created")
            self.strbases = "NULL"
        elif not self.valid_sequence():
            self.strbases = "ERROR"
            print("ERROR!")
        else:
            self.strbases = strbases
            print("New sequence created!")

    def __str__(self):#funcion que me printea como str mi sequencia
        return self.strbases

    def len(self): #metodo que cuenta
        return len(self.strbases)
    def len_null_error(self):
        new_len = ""
        if seq == "NULL" or seq == "ERROR":
            len(new_len)
        return len(new_len)

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def count_bases(self):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        try:
            for b in self.strbases:  # assuming que el seq esta bien
                d[b] = d[b] + 1
        except KeyError:
            d =  {"A": 0, "C": 0, "G": 0, "T": 0}
        return d





