import pandas as pd
from Avl_tree import AVLTree
import timeit
import time 
data_reader_pandas = pd.read_csv('random_numbers.csv', delimiter=' \n', header=None).values.tolist()
# tree = AVLTree()
#print(data_reader_pandas)
Data_set_list = []

for i in range (len(data_reader_pandas)):
    Data_set_list.append(int(data_reader_pandas[i][0]))


tre = AVLTree()
t1 = time.time()
for i in Data_set_list:
    tre.insert(i)
t2 = time.time() 
final = t2-t1 
print (final)



#     # key = row['key_column_name']
#     # value = row['value_column_name']
#     # tree.insert(key, value)



#print(tre.search(8177))
