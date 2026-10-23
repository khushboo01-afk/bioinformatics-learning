sequences = {}
header = None
with open ("sample.fasta","r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):
            header = line[1:]
            if header not in sequences:
              sequences[header]=""

        else :
            if header is not None:
                sequences[header]= sequences[header] +line
            else:
                print("WARNING:DNA sequence found prior to header.")

print(sequences)                 


