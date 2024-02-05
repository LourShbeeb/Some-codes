# open the .txt file and extract data from it.
with open("Restriction.txt") as Data_file:
    Data = Data_file.readlines()
DNA_seq = ""
for i in range(1, len(Data)):
    DNA_seq += Data[i].strip()
print("The given DNA sequence is:", DNA_seq, sep='\n')
# the code below will find the position and length of every reverse palindrome in the DNA string having length between 4 and 12
str1 = 'ATGC'
str2 = "TACG"
print("position   length(bp)")
for seg in range(len(DNA_seq)):
    for base in range(4, 13, 2):
        short_seg = DNA_seq[seg: seg + base]
        # checking if the short segment is reverse palindrome or not!
        if short_seg == short_seg[:: -1].translate(str.maketrans(str1, str2)): 
            if len(DNA_seq[seg: seg + base]) < 4:
                break
            # print the results one by one
            print("{:03d}".format(seg + 1), "         ", len(DNA_seq[seg: seg + base])) 
            if len(DNA_seq) - len(DNA_seq[: seg]) < 12:
                break
                