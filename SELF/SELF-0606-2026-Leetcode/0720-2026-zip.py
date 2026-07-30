list_a=[1, 2, 3 ]
list_b = ['a','b','c']
list_c=list(zip(list_a, list_b))
# [(1, 'a'), (2, 'b'), (3, 'c')]
print(list_c)
 
list_d=[]
list_e=[]
# "Pythonic" way to UNZIP uusing the unpacking operator 
list_d, list_e = zip(*list_c)
# (1, 2, 3)
print(list_d)
# ('a', 'b', 'c')
print(list_e)