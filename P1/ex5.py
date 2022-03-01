from seq1 import seq
null_seq = seq()
valid_seq = seq("ACGTA")
invalid_seq = seq("DFUHNAAACCGGT")
print("sequence1:", valid_seq, "length:", valid_seq.len())
for k,v in valid_seq.count_bases().items():
    print( k + ":", v)

print("sequence2:", null_seq, "length:", null_seq.len_null_error())
for k,v in null_seq.count_bases().items():
    print( k + ":", v)

print("sequence3:", invalid_seq, "length:", invalid_seq.len_null_error())
for k,v in invalid_seq.count_bases().items():
    print( k + ":", v)

