#Crash Course p55-60
def counter(number):
  for value in range(number):
    print(value)
    
counter(5) #prints 0,1,2,3,4

# make list of even numbers 1-100
numbers=list(range(2,100,2))
print(numbers)

# make a list of squares of numbers 1-10
squares=[]
for num in range(1,11):
  squares.append(num * num)
  
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

for i in range(1,21):
  print(i)
  
million=list(range(1,1_000_001))
# print (million)
print(max(million))
print(sum(million))

# Use third argument range f()
oddies=list(range(1,20,2))
print(oddies)

#multiples of three solution1
three_multiples=[]
for i in range(3,31):
  if i % 3 == 0:
    three_multiples.append(i) 
print(three_multiples)

#multiples of three solution2
test = list(range(3,31,3))
for i in test:
  print(i)