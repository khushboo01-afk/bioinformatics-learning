def read_fasta(filename):
  sequences = {}
  header = None

  try:
        with open (filename,"r") as file:
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

  except FileNotFoundError:
     print(f"ERROR: FASTA file'{filename} was not found.")
     return None
     
  return sequences  


if __name__ == "__main__":
    result = read_fasta("sample.fasta")
    print(result)