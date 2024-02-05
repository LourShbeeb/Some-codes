# open the .txt file and extract data from it.
with open("GC.txt") as Data_file:
    Data = Data_file.readlines()
# format the FASTA data in a tidy and readable form (I chose to format them in a dictionary in this case)
IDs_num = 0
DNA_strings = dict()
for line in Data:
    if line.startswith(">"):
        IDs_num += 1
        ID = line.strip()[1:]
        DNA_strings[ID] = ""
    else:
        DNA_strings[ID] += line.strip()
# Now we have a dictionary where keys are the rosalind ID and values are the specific DNA sequence for each Rosalind ID
# you can try: print(DNA_strings), to view the new form of the data
# calculate the GC percentage in each unique sequence and store them in a dictionary
GC_dic = dict()
for ID in DNA_strings.keys():
    GC_content = 0
    for nuc in DNA_strings[ID]:
        if nuc.upper() == "G" or nuc.upper() == "C":
            GC_content += 1
    GC_dic[ID] = round(GC_content / len(DNA_strings[ID]) * 100, 6)
print(GC_dic)
# finding the highest GC percent and print it out
max_GC_perc = max(GC_dic.values())
for ID in GC_dic.keys():
    if GC_dic[ID] == max_GC_perc:
        print("The highest GC percent is located in:", ID)
        print("Its GC percent is: ", GC_dic[ID], "%", sep="")
        break