# open the .txt file and extract data from it.
with open("Cons.txt") as Data_file:
    Data = Data_file.readlines()
# format the FASTA data in a tidy and readable form (I chose to format them in a list in this case)
num_of_fragment = -1
list_of_fragments = list()
for line in range(len(Data)):
    if Data[line].startswith(">"):
        num_of_fragment += 1
        list_of_fragments.append("")
    else:
        list_of_fragments[num_of_fragment] += Data[line].strip()
num_of_fragments = len(list_of_fragments)
frag_length = len(list_of_fragments[0])
# now I will print the number of fragments, the lenght of any DNA fragments and the first 2 fragments of the Dataset to show how it becomes
print("The number of DNA fragments is: {}".format(num_of_fragments), "The length of each DNA fragment is: {} bp".format(frag_length),
      *list_of_fragments[: 2], sep="\n")
# now I will define list of length frag_list contain zeros for the 4 types of DNA nucleotides
A_list = [0] * frag_length
C_list = [0] * frag_length
G_list = [0] * frag_length
T_list = [0] * frag_length
# now this code will produce the profile matrix of the DNA fragments collection
for fragment in range(num_of_fragments):
    for nuc in range(frag_length):
        if list_of_fragments[fragment][nuc] == "A":
            A_list[nuc] += 1
        elif list_of_fragments[fragment][nuc] == "C":
            C_list[nuc] += 1
        elif list_of_fragments[fragment][nuc] == "G":
            G_list[nuc] += 1
        elif list_of_fragments[fragment][nuc] == "T":
            T_list[nuc] += 1
# next this code will produce the consensus DNA string
Consensus = ""
for nuc in range(frag_length):
    max_nuc = max(A_list[nuc], C_list[nuc], G_list[nuc], T_list[nuc])
    if A_list[nuc] == max_nuc:
        Consensus += "A"
    elif C_list[nuc] == max_nuc:
        Consensus += "C"
    elif G_list[nuc] == max_nuc:
        Consensus += "G"
    elif T_list[nuc] == max_nuc:
        Consensus += "T"
# next I will print the results: Consensus DNA sequence and profile matrix
print("The consensus DNA sequence is:\n", Consensus, sep="")
print("\nThe profile matrix for this collection of DNA fragments is:")
print("A:", *A_list)
print("C:", *C_list)
print("G:", *G_list)
print("T:", *T_list)