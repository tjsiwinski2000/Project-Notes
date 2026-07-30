numbers = [1, 2, 3]
letters = ["a", "b", "c"]
zipped = zip(numbers, letters)

print(type(zipped))
#<zip object at 0x7fa4831153c8>

print(list(zipped))
#[(1, 'a'), (2, 'b'), (3, 'c')]