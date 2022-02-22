class seq:
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
    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

