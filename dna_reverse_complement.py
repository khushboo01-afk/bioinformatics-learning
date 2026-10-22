dna="ATGCCGTA"
complement={"A" : "T","T" : "A","C" : "G","G" : "C"}
comp_seq="".join(complement[base] for base in dna)
reverse_seq = comp_seq[::-1]
print(reverse_seq)

