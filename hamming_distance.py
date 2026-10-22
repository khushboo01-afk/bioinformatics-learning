dna_seq1=input("Enter the first DNA sequence: ").strip().upper()
dna_seq2=input("Enter the second DNA sequence:  ").strip().upper()

count = 0

if len(dna_seq1)==0 or len(dna_seq2)==0:
    print("ERROR :DNA sequence can't be empty")

elif any (base not in "ATGC"  for base in dna_seq1 + dna_seq2 ):
    print("Please enter a valid  DNA sequence using A,T,G and C only!")

elif len(dna_seq1) != len(dna_seq2):
    print("Both  DNA sequences must have equal length")

else:
    for i in range(len(dna_seq1)):
        if dna_seq1[i] != dna_seq2[i]:
          count += 1

        print("DNA sequence 1: ",dna_seq1)  
        print("DNA sequence 2: ",dna_seq2) 
        print("Hamming distance : ",count)       
