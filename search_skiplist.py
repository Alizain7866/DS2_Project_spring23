## TODO find the complexity of searching
# Generating random numbers that exist inside the CSV and searching them in the AVL Tree


import pandas as pd
from Skip_list import SkipList
import random
import timeit
import time 
data_reader_pandas = pd.read_csv('dataset_correct.csv', delimiter=' \n', header=None).values.tolist()
# tree = SkipList()
#print(data_reader_pandas)
Data_set_list = []
output_list = []

#1000

for i in range (len(data_reader_pandas)):
    Data_set_list.append(int(data_reader_pandas[i][0]))

#Data_set_list.sort()
#Data_set_list.sort(reverse = True)

insert_num_1000 = 1000
tre_1000 = SkipList()
for i in range(insert_num_1000):
    tre_1000.insert(Data_set_list[i],[i])

r_numbers = [random.randint(1, 10000) for _ in range(1000001)]

# 1000

Initial_time_1000 = time.time()
for i in range(insert_num_1000):
    tre_1000.search(r_numbers[i])
stopTime_1000 = time.time() 
final_time_1000 = stopTime_1000-Initial_time_1000 
print ("The time to search_num_1000 is :",final_time_1000)

output_list.append((insert_num_1000,final_time_1000))


# 5000

insert_num_5000 = 5000
tre_5000 = SkipList()
for i in range(insert_num_5000):
    tre_5000.insert(Data_set_list[i],[i])

Initial_time_5000 = time.time()
for i in range(insert_num_5000):
    tre_5000.search(r_numbers[i])
stopTime_5000 = time.time() 
final_time_5000 = stopTime_5000-Initial_time_5000 
print ("The time to search_num_5000 is :",final_time_5000)

output_list.append((insert_num_5000,final_time_5000))

# 10000

insert_num_10k = 10000
tre_10k = SkipList()
for i in range(insert_num_10k):
    tre_10k.insert(Data_set_list[i],[i])

Initial_time_10k = time.time()
for i in range(insert_num_10k):
    tre_10k.search(r_numbers[i])
stopTime_10k = time.time() 
final_time_10k = stopTime_10k-Initial_time_10k 
print ("The time to search_num_10k is :",final_time_10k)

output_list.append((insert_num_10k,final_time_10k))


# 50k

insert_num_50k = 10000
tre_50k = SkipList()
for i in range(insert_num_50k):
    tre_50k.insert(Data_set_list[i],[i])

Initial_time_50k = time.time()
for i in range(insert_num_50k):
    tre_50k.search(r_numbers[i])
stopTime_50k = time.time() 
final_time_50k = stopTime_50k-Initial_time_50k 
print ("The time to search_num_50k is :",final_time_50k)

output_list.append((insert_num_50k,final_time_50k))


# 100k

insert_num_100k = 100000
tre_100k = SkipList()
for i in range(insert_num_100k):
    tre_100k.insert(Data_set_list[i],[i])

Initial_time_100k = time.time()
for i in range(insert_num_100k):
    tre_100k.search(r_numbers[i])
stopTime_100k = time.time() 
final_time_100k = stopTime_100k-Initial_time_100k 
print ("The time to search_num_100k is :",final_time_100k)

output_list.append((insert_num_100k,final_time_100k))


# 500k

insert_num_500k = 500000
tre_500k = SkipList()
for i in range(insert_num_500k):
    tre_500k.insert(Data_set_list[i],[i])

Initial_time_500k = time.time()
for i in range(insert_num_500k):
    tre_500k.search(r_numbers[i])
stopTime_500k = time.time() 
final_time_500k = stopTime_500k-Initial_time_500k 
print ("The time to search_num_500k is :",final_time_500k)

output_list.append((insert_num_500k,final_time_500k))


# 1M

insert_num_1M = 500000
tre_1M = SkipList()
for i in range(insert_num_1M):
    tre_1M.insert(Data_set_list[i],[i])

Initial_time_1M = time.time()
for i in range(insert_num_1M):
    tre_1M.search(r_numbers[i])
stopTime_1M = time.time() 
final_time_1M = stopTime_1M-Initial_time_1M 
print ("The time to search_num_1M is :",final_time_1M)

output_list.append((insert_num_1M,final_time_1M))