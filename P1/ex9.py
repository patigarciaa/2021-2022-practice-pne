import seq1
s1 = seq1.seq()
s1.read_fasta("../session04/U5")

print("Sequence1 (Length):", s1.len(), s1)
print("bases:", s1.count_bases())
print("Reverse:",s1.seq_reverse())
print("complement:",s1.seq_complement())