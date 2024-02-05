# at the begginning we will import comb (combinations) function from math libray
from math import comb
with open("Mend.txt") as Data_file:
    Data = Data_file.readline().strip()
k, m, n = map(int, Data.split(" "))
print("homozygous dominant number:", k, ", heterozygous number:", m, ", homozygous recessive number:", n)
# calculate the total probable groups number
total = comb(m + n + k, 2)
print("Total possible groups is:", total)
