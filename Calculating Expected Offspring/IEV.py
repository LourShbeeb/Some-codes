# open the .txt file and extract data from it.
with open("IEV.txt") as Data_file:
    Data = Data_file.readline().strip()
event_1, event_2, event_3, event_4, event_5, event_6 = map(int, Data.split(" "))
print(event_1, event_2, event_3, event_4, event_5, event_6)
# this function will calculate the expected number of offspring displaying the dominant phenotype in the next generation
def expected_num(events_of_prob_1_00, events_of_prob_0_75, events_of_prob_0_5):
    total = 2 * (events_of_prob_1_00 + 0.75 * events_of_prob_0_75 + 0.5 * events_of_prob_0_5)
    return total
print(" The expected number of offspring displaying the dominant phenotype in the next generation is:", 
      expected_num(event_1+event_2+event_3, event_4, event_5))
