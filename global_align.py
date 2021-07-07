#################################
# Sequeneces global alignment. Identity calculator.
### Finds the species with the highest identity with an unknown sequence.
### The unknown sequence and the sequences from the database must be given 
### in two separate fasta files (one for unknown and other for the database),
### both stored in the working directory.
### Requires that sequences have the same length.
# Author: Berta Gallego
# Date: 2021-07-07
# Usage: python3 file_name.py
### Uses Python 3. No external libraries required.
##################################
import sys

def sequences_dict(file_name):
    """
    Open a text file with the sequences 
    and store them in a dictionary with format
    {species_name_1: sequence_1, species_name_2: sequence_2}
    """
    try:
        seq_dict = {}
        with open(file_name, "r") as fasta:
            for line in fasta:
                line = line.rstrip()
                if line.startswith(">"):
                    key = line[1:]
                    seq_dict[key] = ""
                else:
                    seq_dict[key] = seq_dict[key] + line
        return seq_dict
    except:
        print("Please, provide x.fasta and database.fasta.")
        sys.exit()

def compare_sequences(unknown, database):
    """
    Compare sequence from unknown sample 
    with each of the sequences from the database
    and calculate identities.
    Show the first species with the highest identity.
    """
    sequence1, = unknown.values()
    l1 = len(sequence1)
    highest_identity = 0
    highest_identity_sp = ""
    for species_name in database:
        sequence2 = database[species_name]
        l2 = len(sequence2)
        if l1 == l2:
            match = 0
            for base1, base2 in zip(sequence1, sequence2):
                if base1 == base2:
                    match += 1
            identity = match*100/l1
            if identity > highest_identity:
                highest_identity = identity
                highest_identity_sp = species_name
            print(f">>{species_name} has a {round(identity,2)}% of identity with unknown sample.")
        else:
            print("Sequences don't have the same length.")
    print(f"""
          ********************************************************************
           {highest_identity_sp} has the highest identity ({round(highest_identity,2)}%)
          ********************************************************************
          """)

if __name__ == "__main__":

    print("""
=============================
 GLOBAL ALIGNMENTS
 Identity between sequences
=============================
    """)
    # Get the data
    unknown = sequences_dict("x.fasta")
    database = sequences_dict("database.fasta")

    # Compare sequences
    compare_sequences(unknown, database)
