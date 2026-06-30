# Print a list of all possible coordinates given by on a 3D grid x,y,z
# where the sum of is not equal to n 
# Please use list comprehensions rather than multiple loops, as a learning exercise. 
x = int(input())
y = int(input())
z = int(input())
n = int(input())

#phase1 - create all permutations of x,y,z using list comprhension
from itertools import permutations
        
input_list = [0,0,0,x,y,z]
#phase2 - create our list , note: [set] removes duplicates
my_list = [[x for x in item] for item in set(permutations(input_list,3)) if sum(item) !=n ]
print(sorted(my_list))

# Example input: 1,1,2,3
# Example output: 
# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 2, 0], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2], [1, 2, 1], [2, 0, 0], [2, 1, 1]]