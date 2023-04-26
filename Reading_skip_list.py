import pandas as pd
from Skip_list import SkipList
import timeit
import time 
df = pd.read_csv('random_numbers_10k.csv', delimiter=' \n', header=None).values.tolist()
# tree = AVLTree()
#print(df)
news = []

for i in range (len(df)):
    news.append(int(df[i][0]))


tre = SkipList()
t1 = time.time()
for i in news:
    tre.insert(i)
t2 = time.time() 
final = t2-t1 
print (final)
