# dictionary practice
fruits = {"apple":2, "pear" : 1, "pineaple" : 3, "peach" : 1 , "zebra" : 0 }

# return fruit with highest key e.g. pineapple 3
print(max(fruits,key=fruits.get))

# return fruit with "highest" name  e.g. zebra 
print(max(fruits))