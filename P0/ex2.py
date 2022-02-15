
import seq0
filename = seq0.valid_filename()
f = seq0.seq_read_fasta(filename)
print(f[0:20])