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


news.sort()

