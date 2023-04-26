import pandas as pd
from Avl_tree import AVLTree
import timeit
import time 
data_reader_pandas = pd.read_csv('dataset_correct.csv', delimiter=' \n', header=None).values.tolist()
# tree = AVLTree()
#print(data_reader_pandas)
Data_set_list = []

for i in range (len(data_reader_pandas)):
    Data_set_list.append(int(data_reader_pandas[i][0]))

insert_num_1000 = 1000
tre_1 = AVLTree()
Initial_time_1000 = time.time()
for i in range(insert_num_1000):
    tre_1.insert(Data_set_list[i])
stopTime_1000 = time.time() 
final_time_1000 = stopTime_1000-Initial_time_1000 
print ("The time to insert_num_1000 is :",final_time_1000)


# #second AVL
# tre_ = AVLTree()
# t1 = time.time()
# for i in Data_set_list:
#     tre.insert(i)
# t2 = time.time() 
# final = t2-t1 
# print (final)


#Third AVL
# tre = AVLTree()
# t1 = time.time()
# for i in Data_set_list:
#     tre.insert(i)
# t2 = time.time() 
# final = t2-t1 
# print (final)







#     # key = row['key_column_name']
#     # value = row['value_column_name']
#     # tree.insert(key, value)



#print(tre.search(8177))
