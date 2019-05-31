import string

dna_letters = "ATGC"
rna_letters = "UACG"
rna = string.maketrans(dna_letters, rna_letters)

dna = raw_input("Good evening. Please kindly tell me your DNA? ")
print dna.translate(rna)