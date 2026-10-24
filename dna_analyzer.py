from read_fasta import read_fasta
def validate_dna(sequence):
    sequence = sequence.strip().upper()

    if not sequence:
        return False
    
    for base in sequence:
        if base not in "ATGC":
            return False
    return True 

def count_nucleotide(sequence):
    sequence = sequence.strip().upper()

    count = {
        "A" : sequence.count("A"),
        "T" : sequence.count("T"),
        "G" : sequence.count("G"),
        "C" : sequence.count("C")
    }
    return count

def length_calculate(sequence):
    return len(sequence)

def calculate_gc_content(sequence):
    sequence = sequence.upper()

    if not sequence:
        return 0.0

    
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percentage =(gc_count/len(sequence))*100

    return gc_percentage

def transcribe_dna_to_rna(sequence):
    sequence = sequence.upper()
    return sequence.replace("T","U")

def reverse_complement(sequence):
    sequence = sequence.upper()

    complement={"A" : "T","T" : "A","C" : "G","G" : "C"}
    comp_seq="".join(complement[base] for base in sequence)
    reverse_seq = comp_seq[::-1]
    return reverse_seq

def find_motif(sequence,motif):
    sequence = sequence.upper()
    motif = motif.upper()

    if not sequence:
        print("ERROR :DNA sequence can't be empty")
        return []

    elif  not motif :
        print("ERROR :DNA substring can't be empty")  
        return []

    positions = []

    
    for i in range(len(sequence)-len(motif)+1):
            if sequence[i:i+len(motif)]== motif:
               positions.append(i+1)
    return positions

def calculate_hamming_distance(sequence_a,sequence_b):
    sequence_a = sequence_a.upper()
    sequence_b = sequence_b.upper()

    if len(sequence_a) != len(sequence_b):
        print("ERROR : DNA sequences must be  of same length.")
        return None

    distance = 0
    for base in range(len(sequence_a)):
        if sequence_a[base] != sequence_b[base]:
         distance += 1
    return distance

def analyze_dna(sequence,motif):
     sequence = sequence.upper()
     motif = motif.upper()
     
     if not validate_dna(sequence):
         print("ERROR : Invalid  DNA sequence.")
         return None

     if not motif.strip():
         print("ERROR: DNA motif cannot be empty.")
         return None
     
     if not validate_dna(motif):
              print("ERROR : Invalid  DNA motif.")
              return None

     results ={
        "Sequence": sequence,
        "Length": length_calculate(sequence),
        "Nucleotide counts": count_nucleotide(sequence),
        "GC content": calculate_gc_content(sequence),
        "RNA sequence": transcribe_dna_to_rna(sequence),
        "Reverse complement": reverse_complement(sequence),
        "Motif positions":find_motif(sequence,motif),
        "Motif count":len(find_motif(sequence,motif))
    }
     return results
if __name__ =="__main__":
    fasta_sequence = read_fasta("sample.fasta")

    if fasta_sequence is None:
        print("ERROR: Could not read the FASTA file.")
    elif not fasta_sequence:
     print("ERROR:No sequences found in FASTA file.")    
    else:    
        print("Available sequences.")
        for header in fasta_sequence:
            print(header)
        selected_header = input("Enter the sequence name you want to analyze.")    
        if selected_header in fasta_sequence:
            sequence = fasta_sequence[selected_header]

            print("Selected DNA sequence: ",sequence)

            if not validate_dna(sequence):
                print("ERROR: Invalid DNA sequence.")

            else:
              motif = input("Enter a  DNA motif  to search for: ")
              report = analyze_dna(sequence,motif)
            
            if report is not None:
                    print("\nDNA SEQUENCE ANALYSIS")
                    print("---------------------")
                    print("Sequence:", report["Sequence"])
                    print("Length:", report["Length"])
                    print("Nucleotide counts:", report["Nucleotide counts"])
                    print("GC content:", f'{report["GC content"]:.2f}%')
                    print("RNA sequence:", report["RNA sequence"])
                    print("Reverse complement:", report["Reverse complement"])
                    print("Motif positions",report["Motif positions"])
                    print("Motif count",report["Motif count"])
            else:
                    print("Analysis could not be completed. ")  
        else:
                print("ERROR: Sequence name not found.")
