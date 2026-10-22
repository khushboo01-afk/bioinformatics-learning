dna= input("Enter a dna sequence: ").strip().upper()
if len(dna)==0:
    print("ERROR :DNA sequence can't be empty")

elif any (base not in "ATGC"  for base in dna ):
    print("Please enter a valid  DNA sequence using A,T,G and C only!")
else:
   rna = dna.replace("T","U")
   print(rna)