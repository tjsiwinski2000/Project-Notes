# 0107-2026 TJS: This was very hard
# You are given a 2-D array of size N X M
# Your task is to find:
# -The mean along axis 1
# -The var along axis 0
# -The std along axis None
import numpy
def mean_tool(input_array, axis_value):
    print(numpy.mean(input_array,axis=axis_value))
    
def var_tool(input_array, axis_value):
    print(numpy.var(input_array,axis=axis_value))

def std_tool(input_array):
    print(round(numpy.std(my_array, axis = None),11))

#Note: solution fails if you have prompts for user input.
first_line= input()
n=int(first_line.split()[0]) #n - number of lines
m=int(first_line.split()[1]) #m - number of numbers in each line

# Phase1 - build an array of arrays e.g. [[1, 2], [3, 4]]
my_array = []
for count in range(1,n+1):
    line = input()
    temp=[]
    for num in line.split():
        temp.append(int(num))
    my_array.append(temp)
    
# Phase2 - convert array to numpy array
my_array = numpy.array(my_array)
# Phase3 - get various numpy outputs.
mean_tool(my_array,1)
var_tool(my_array,0)
std_tool(my_array)