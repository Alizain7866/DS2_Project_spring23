## TODO find the complexity of the root node
#find the complexity of the left most leaf node 
#find the complexity of the right most leaf node



import pandas as pd
from Skip_list import SkipList
import timeit
import time 
data_reader_pandas = pd.read_csv('dataset_correct.csv', delimiter=' \n', header=None).values.tolist()
# tree = AVLTree()
#print(data_reader_pandas)
Data_set_list = []
output_list = []

#Data_set_list.sort()
Data_set_list.sort(reverse = True)

for i in range (len(data_reader_pandas)):
    Data_set_list.append(int(data_reader_pandas[i][0]))

#1000

insert_num_1000 = 1000
tre_1000 = SkipList()
Initial_time_1000 = time.time()
for i in range(insert_num_1000):
    tre_1000.insert(Data_set_list[i])
stopTime_1000 = time.time() 
final_time_1000 = stopTime_1000-Initial_time_1000 
print ("The time to insert_num_1000 is :",final_time_1000)
print(tre_1000.max_height)
output_list.append((insert_num_1000,final_time_1000))



# 5000



insert_num_5000 = 5000
tre_5000 = SkipList()
Initial_time_5000 = time.time()
for i in range(insert_num_5000):
    tre_5000.insert(Data_set_list[i])
stopTime_5000 = time.time() 
final_time_5000 = stopTime_5000-Initial_time_5000 
print ("The time to insert_num_5000 is :",final_time_5000)
print(tre_5000.max_height)

output_list.append((insert_num_5000,final_time_5000))


#10000

insert_num_10000 = 10000
tre_10000 = SkipList()
Initial_time_10000 = time.time()
for i in range(insert_num_10000):
    tre_10000.insert(Data_set_list[i])
stopTime_10000 = time.time() 
final_time_10000 = stopTime_10000-Initial_time_10000
print ("The time to insert_num_10000 is :",final_time_10000)
print(tre_10000.max_height)

output_list.append((insert_num_10000,final_time_10000))


#50k


insert_num_50000 = 50000
tre_50000 = SkipList()
Initial_time_50000 = time.time()
for i in range(insert_num_50000):
    tre_50000.insert(Data_set_list[i])
stopTime_50000 = time.time() 
final_time_50000 = stopTime_50000-Initial_time_50000 
print ("The time to insert_num_50k is :",final_time_50000)
print(tre_50000.max_height)

output_list.append((insert_num_50000,final_time_50000))



# #100k

insert_num_100k = 100000
tre_100k = SkipList()
Initial_time_100k = time.time()
for i in range(insert_num_100k):
    tre_100k.insert(Data_set_list[i])
stopTime_100k = time.time() 
final_time_100k = stopTime_100k-Initial_time_100k 
print ("The time to insert_num_100k is :",final_time_100k)
print(tre_100k.max_height)

output_list.append((insert_num_100k,final_time_100k))

#500k
insert_num_500k = 500000
tre_500k = SkipList()
Initial_time_500k = time.time()
for i in range(insert_num_500k):
    tre_500k.insert(Data_set_list[i])
stopTime_500k = time.time() 
final_time_500k = stopTime_500k-Initial_time_500k 
print ("The time to insert_num_500k is :",final_time_500k)
print(tre_500k.max_height)

output_list.append((insert_num_500k,final_time_500k))

# 1M
insert_num_1M = 1000000
tre_1M = SkipList()
Initial_time_1M = time.time()
for i in range(insert_num_1M):
    tre_1M.insert(Data_set_list[i])
stopTime_1M = time.time() 
final_time_1M = stopTime_1M-Initial_time_1M 
print ("The time to insert_num_1M is :",final_time_1M)
print(tre_1M.max_height)

output_list.append((insert_num_1M,final_time_1M))
