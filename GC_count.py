def calaculate_gc_content(dna):
    dna=dna.upper()

    g_count = dna.count("G")
    c_count = dna.count("C")
    total_bases = len(dna)

    gc_content=((g_count+c_count)/total_bases)*100
    return gc_content

dna= input("Enter a DNA sequence: ").strip().upper()
if len(dna)==0:
    print("ERROR :DNA sequence can't be empty")

elif any (base not in "ATGC"  for base in dna ):
    print("Please enter a valid  DNA sequence using A,T,G and C only!")
else:
    result=calaculate_gc_content(dna)
    print("DNA sequence :" ,dna)    
    print("GC content: ",result,"%")