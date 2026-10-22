def count_substring(dna,motif):
    dna = dna.upper()
    motif = motif.upper()

    count = 0

    for i in range(len(dna)-len(motif)+1):
        if dna[i:i+len(motif)]== motif:
           count += 1
    return count
   
dna = input("Enter a DNA sequence: ").strip().upper()
motif = input("Enter a DNA substring : ").strip().upper()


if len(dna)==0:
    print("ERROR :DNA sequence can't be empty")

elif any (base not in "ATGC"  for base in dna ):
    print("Please enter a valid  DNA sequence using A,T,G and C only!")

elif len(motif)==0:
    print("ERROR :DNA substring can't be empty")

elif any (base not in "ATGC"  for base in motif ):
    print("Please enter a valid  DNA substring using A,T,G and C only!")    
else:
    result= count_substring(dna,motif)
    print("DNA sequence : ", dna )
    print("Motif : ", motif )
    print("Occurrences: ", result)