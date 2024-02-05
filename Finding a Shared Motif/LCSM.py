# import random library
import random
# open the .txt file and extract data from it.
with open("LCSM.txt") as Data_file:
    Data = Data_file.readlines()
# format the FASTA data in a tidy and readable form (I chose to format them in a list in this case) and sort the strings by their length
IDs_num = -1
list_of_seq = list()
for line in Data:
    if line.startswith(">"):
        IDs_num += 1
        list_of_seq.append("")
    else:
        list_of_seq[IDs_num] += line.strip()
list_of_seq.sort(key=len)
number_of_fragments = len(list_of_seq)
# this code below will find the longest common substring of the DNA strings collection
sug_long = random.randint(50, 100) # suggested long of the substring
N_of_occ = 0
x = True
while x is True:
    z = 0
    for i in range(len(list_of_seq[0]) - sug_long + 1):
        z = 0
        for j in range(1, number_of_fragments):
            if list_of_seq[0][i: i+sug_long] in list_of_seq[j]:
                z += 1
        if z == number_of_fragments - 1:
            sug_long += 1
            N_of_occ += 1
        else:
            if N_of_occ == 1:
                print("The longest common substring of the DNA strings collection is:")
                print(list_of_seq[0][i - 1: i + sug_long - 2])
                x = False
                break
            elif N_of_occ >1:
                print("The longest common substring of the DNA strings collection is:")
                print(list_of_seq[0][i - N_of_occ: i + sug_long - 2])
                x = False
                break
    sug_long -= 1