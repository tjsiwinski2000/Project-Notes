# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.
#https://leetcode.com/problems/count-the-number-of-special-characters-i/?envType=daily-question&envId=2026-06-18

#  Example 1:
# Input: word = "aaAbcBC"
# Output: 3
# Explanation:
# The special characters in word are 'a', 'b', and 'c'.

# Example 2:
# Input: word = "abc"
# Output: 0
# Explanation:
# No character in word appears in uppercase.

# Example 3:
# Input: word = "abBCab"
# Output: 1
# Explanation:
# The only special character in word is 'b'.

#Input = "CCc" 
#Output: 1  note: test case 602 ✅ fixed

#Input = "aaAbcBC"
#Output: 3 note test case 697 ❌my output:2 [12:20pm-0620-2026]
#TESTING my_list= [97, 97, 65, 98, 99, 66, 67]
#TESTING  my_list.count(97)

# Constraints:
# 1 <= word.length <= 50
# word consists of only lowercase and uppercase English letters.

#0621-2026 found a simplified solution (below)


class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Complete list of ascii for word passed to function
        ascii_list = ([ord(letter) for letter in word])
        # List of Capitals with Matching small letter
        matches = [num for num in ascii_list if num-32 in ascii_list]
        #Removing duplicates
        return len(list(set(matches)))
    
my_obj = Solution()
print(f'abBCab" {my_obj.numberOfSpecialChars("abBCab")}')
print(f'aaAbcBC: {my_obj.numberOfSpecialChars("aaAbcBC")}')
print(f'CCc:{my_obj.numberOfSpecialChars("CCc")}')