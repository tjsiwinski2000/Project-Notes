# Given a string s, find the length of the longest without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def find_dup(s):
    for char in s:
        if s.count(char) > 1:
            return True
    return False

def longest_sub_string(s):
    # store current max length of letters w/o repearts
    max_length=0
    # store current max word
    max_word = ""
    # store length of string
    s_length = len(s)
    # for each letter in string
    for num in range(0,s_length):
        # iterate thr. every "word" length, starting w.that letter
        for num2 in range(num+1,s_length+1):
            temp =  s[num:num2]
            # print(temp)
            if find_dup(temp) == False:
                if max_length < len(temp):
                    max_length = len(temp)
                    max_word = temp
                    print(f'max_length now {max_length}. max_word now {max_word}')
    return(max_word)
    # return letter 

s = "abcabzxcbb"
print(f'longest sub string for {s} is {longest_sub_string(s)}')
# print(find_dup(s))
s = "bbbbb"
print(f'longest sub string for {s} is {longest_sub_string(s)}')

s = "pwwkew"
print(f'longest sub string for {s} is {longest_sub_string(s)}')