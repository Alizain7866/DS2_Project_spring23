import pandas as pd
from Avl_tree import AVLTree
import timeit
import time 
data_reader_pandas = pd.read_csv('dataset_correct.csv', delimiter=' \n', header=None).values.tolist()
# tree = AVLTree()
#print(data_reader_pandas)
Data_set_list = []
output_list = []


for i in range (len(data_reader_pandas)):
    Data_set_list.append(int(data_reader_pandas[i][0]))

Data_set_list.sort()

