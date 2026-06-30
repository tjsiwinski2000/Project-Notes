# Without using Python's built-in .title() method, write a single line of code
# (a lambda function or a list comprehension) that takes a lowercase sentence and capitalizes the first letter of every word.

# Input: "the quick brown fox jumps over the lazy dog"

# Expected Output: "The Quick Brown Fox Jumps Over The Lazy Dog"


in_string = "the quick brown fox jumps over the lazy dog"

print([chr(ord(item[0])-32)+item[1:] for item in in_string.split(' ')])



#SOLUTION
# That is a fantastic effort! You nailed the list comprehension logic.

# Your solution correctly splits the string, grabs the first character, shifts its ASCII value by -32 to convert it to uppercase (very clever low-level trick!), and glues it back to the rest of the word.

# There is just one tiny catch: it returns a list of strings instead of a single string, and it will crash if there are multiple spaces in a row (because item[0] on an empty string "" throws an IndexError).

# Here is how you can turn your exact logic into a fully working, robust one-liner using ' '.join():
print(' '.join([chr(ord(w[0]) - 32) + w[1:] for w in in_string.split()]))