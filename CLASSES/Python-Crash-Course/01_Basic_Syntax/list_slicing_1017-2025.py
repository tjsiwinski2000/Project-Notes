#CrashCourse p60

# list of cubes 1..10
for i in range(1,11):
  print(f"The cube of {i} is {i**3}")
  
# cube comprehension
cubes = []
for value in range(1,11):
  cubes.append(value ** 3)
print(cubes)

# slicing a list
players = ['Rafa', 'Roger', 'Joker', 'Murrary']
print(players[1:3]) 
# ['Roger', 'Joker']

print(players[:4])
# 0 assumed as starting point since starting value ommitted  ['Rafa', 'Roger', 'Joker', 'Murrary']

print(players[2:])
# Max length assumged as end pont, since end point omitted['Joker', 'Murrary']

# practical application of a slice
# -- given a list of test scrores , find the top THREE
test_scores = [100, 98, 42, 55, 66, 97, 75, 80]
# -- step 1 reverse sorr the list
test_scores.sort(reverse = True)
# -- step 2 slice the list 
print(test_scores[:3])