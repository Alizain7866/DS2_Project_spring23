import pandas as pd
from Avl_tree import AVLTree
import timeit
import time 
df = pd.read_csv('random_numbers.csv', delimiter=' \n', header=None).values.tolist()
# tree = AVLTree()
#print(df)
news = []

for i in range (len(df)):
    news.append(int(df[i][0]))


tre = AVLTree()
t1 = time.time()
for i in news:
    tre.insert(i)
t2 = time.time() 
final = t2-t1 
print (final)



#     # key = row['key_column_name']
#     # value = row['value_column_name']
#     # tree.insert(key, value)



#print(tre.search(8177))
