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

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ascii_list = [ord(letter) for letter in word]
        specials = 0
        for num in ascii_list:
            print(f'evaluationg num:{num}')
            if num <= 90:
                match = num +32
                if match in ascii_list:
                    specials +=1
                    print(f'num:{num} match: {match} specials: {specials}, ascii_list: {ascii_list}')
                    # ascii_list.remove(match)
                    print(f'num:{num} match: {match} specials: {specials}, ascii_list: {ascii_list}')
        return specials
    
my_obj = Solution()
# print(my_obj.numberOfSpecialChars("abBCab"))
print(my_obj.numberOfSpecialChars("aaAbcBC"))
print(f'CCc:{my_obj.numberOfSpecialChars("CCc")}')