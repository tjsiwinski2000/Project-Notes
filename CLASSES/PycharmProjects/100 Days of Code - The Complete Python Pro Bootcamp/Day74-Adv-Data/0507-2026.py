import  pandas as pd
from numpy.ma.extras import average

sets = pd.read_csv('./LEGO_NB_DATA/data/sets.csv')
# print(sets.head())
parts_per_set = sets.groupby('year').agg({'num_parts':'mean'})
print(parts_per_set)