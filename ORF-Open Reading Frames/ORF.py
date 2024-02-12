# open the .txt file and extract data from it.
with open("ORF.txt") as Data_file:
    Data = Data_file.readlines()
DNA_str = ""
for line in range(1, len(Data)):
    DNA_str += Data[line].strip()
print(DNA_str)
# this code below will produce a list, which contains the DNA substrings that begins with start codon and ends with stop codon
str_cod = ["ATG"]
stp_cod = ["TAG", "TGA", "TAA"]
seq_for_translate = list()
# looking for ORFs in the direct strand of DNA
for start in range(3):
    for codon1 in range(start, len(DNA_str) - 2, 3):
        if DNA_str[codon1: codon1+3] == str_cod[0]:
            for codon2 in range(codon1, len(DNA_str) - 2, 3):
                if DNA_str[codon2: codon2+3] in stp_cod:
                    break
            if DNA_str[codon1: codon2+3][-3:] in stp_cod:
                seq_for_translate.append(DNA_str[codon1: codon2 + 3])

# looking for ORFs in the reverse strand of DNA
str1 = 'ACGT'
str2 = 'TGCA'
rev_DNA_str = DNA_str[:: -1].translate(str.maketrans(str1, str2))  # produce the reverse complement of the DNA direct strand
for start in range(3):
    for codon1 in range(start, len(DNA_str) - 2, 3):
        if rev_DNA_str[codon1: codon1+3] == str_cod[0]:
            for codon2 in range(codon1, len(DNA_str) - 2, 3):
                if rev_DNA_str[codon2: codon2+3] in stp_cod:
                    break
            if rev_DNA_str[codon1: codon2+3][-3:] in stp_cod:
                seq_for_translate.append(rev_DNA_str[codon1: codon2 + 3])
print("These are the ORFs in the givven DNA sequence:")
print(seq_for_translate)
# the code below will convert the ORFs in DNA to protein
table = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '', 'TAG': '',
    'TGC': 'C', 'TGT': 'C', 'TGA': '', 'TGG': 'W',
}

protein_seq = [""] * len(seq_for_translate)

for seq in range(len(seq_for_translate)):
    for nuc in range(0, len(seq_for_translate[seq]) - 2, 3):
        protein_seq[seq] += table[seq_for_translate[seq][nuc: nuc+3]]
dis_protein_seq = set(protein_seq)
print("\nThe distinct candidate protein strings that can be translated from ORFs of the given DNA string are:\n", *dis_protein_seq, sep='\n')
