# from Claude
# Challenge: Given two lists — one of paths, one of sizes — combine them into a dictionary using one line.

paths = ["c:\\a.txt", "c:\\b.txt", "c:\\c.txt"]
sizes = [30, 100, 5]

# my solution, works 
my_dict = { paths[i]:sizes[i] for i in range(0,3)}

# better not hard coded       
my_dict = {paths[i]: sizes[i] for i in range(len(paths))}

# The zip() version is the more "Pythonic" one 
my_dict = {p: s for p, s in zip(paths, sizes)}
print(my_dict)