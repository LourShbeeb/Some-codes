# at the begginning we will import comb (combinations) function from math libray
from math import comb
with open("IPRB.txt") as Data_file:
    Data = Data_file.readline().strip()
k, m, n = map(int, Data.split(" "))
print("homozygous dominant number:", k, ", heterozygous number:", m, ", homozygous recessive number:", n)
# calculate the total probable groups number
total = comb(m + n + k, 2)
print("Total possible groups is:", total)
# i will list now all the weighted combinations to produce individuals with at least one dominant allele
weighted_comb1 = comb(k+m+n, 2) - comb(m+n, 2)
weighted_comb2 = 0.75 * comb(m, 2)
weighted_comb3 = 0.5 * (comb(m+n, 2) - comb(m, 2) - comb(n, 2))
sum_weighted_combs = weighted_comb1 + weighted_comb2 + weighted_comb3
# The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
probabilty = sum_weighted_combs / total * 100
print("The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele", round(probabilty, 5))
