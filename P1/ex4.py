from seq1 import seq
null_seq = seq()
valid_seq = seq("ACGTA")
invalid_seq = seq("DFUHNAAACCGGT")
print("sequence1:", valid_seq, "length:", valid_seq.len())
print("sequence2:", null_seq, "length:", null_seq.len_null_error())
print("sequence3:", invalid_seq, "length:", invalid_seq.len_null_error())