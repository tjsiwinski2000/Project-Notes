# 0502-2026
# Word Frequency Counter 
# Given a string of text, return a dictionary of each word and how many times 
# it appears, sorted from most to least frequent.

text = "the cat sat on the mat the cat"
my_dict = { item : text.count(item) for item in text.split()}
print(my_dict)

#. Palindrome Checker
#Write a function that returns True if a string is a palindrome, 
# ignoring spaces, punctuation, and capitalization.

#my solution 0501-2026 
def is_palindrome(s):
    s = s.replace(' ','').lower()
    print(s)
    if s == s[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome('hello'))

#claude solution 0501-2026 accomodates punctuation:
import re

def is_palindrome_claude(s):
    s = re.sub(r'[^a-z]', '', s.lower())
    print(s)
    return s == s[::-1]

print(is_palindrome_claude("A man, a plan, a canal Panama"))
print(is_palindrome_claude('hello'))


