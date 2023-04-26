#NEW CODE
# Making dataset of 1000 K 

import random
import csv

# Generate random numbers
numbers = [random.randint(1, 10000) for _ in range(1000001)]

data7 = []

# Save the numbers in a CSV file
def writer() -> None:
    with open('random_numbers_1M.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([num] for num in numbers)

def read(file: str) -> None:
    input_lines = open(file).readlines()
    reader = csv.reader(input_lines)
    for i,row in enumerate(reader):
        if i == 0:
            header = row
            continue
        data7.append(int(row[0]))
        
writer()                       # only for when updating the CSV
read('random_numbers_1M.csv')
print(len(data7))
