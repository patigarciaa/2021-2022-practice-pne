class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        print("New sequence created!")


# Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC") #de esta manera lo que consigo es que me salga lo de "new sequence created"
#pero ahora s1 y s2 tienen atributos attach a ellos (s1 y s2 son objetos) sus atributos son sus sequencias


#metodo str
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")


# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print("Testing....")
#con el str consigo que el programa me printee las sequencias (atributos) de s1 y s2 (objetos)

#ahora añadimos metodos extra como len
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")