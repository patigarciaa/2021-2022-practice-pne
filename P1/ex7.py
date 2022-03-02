from seq1 import seq
null_seq = seq()
valid_seq = seq("ACGTA")
invalid_seq = seq("DFUHNAAACCGGT")
print("sequence1:", valid_seq, "length:", valid_seq.len())
print(valid_seq.count_bases())
print(valid_seq.seq_reverse())

print("sequence2:", null_seq, "length:", null_seq.len_null_error())
print(null_seq.count_bases())
print(null_seq.seq_reverse())

print("sequence3:", invalid_seq, "length:", invalid_seq.len_null_error())
print(invalid_seq.count_bases())
print(invalid_seq.seq_reverse())
