# 1189. Maximum Number of Balloons
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
# https://leetcode.com/problems/maximum-number-of-balloons/?envType=daily-question&envId=2026-06-22


# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

#0622-2026 working solution, not super efficient, not terrible 
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # temp = [f'{letter}:{text.count(letter)}' for letter in 'balon' if letter in text]
        target_word = 'balloon'
        count =0
        word_list = list(text)
        while True:
            for letter in target_word:
                print(f'currently evaluating: {letter}')
                if letter in word_list:
                    word_list.remove(letter)
                    if letter =='n':
                        count+=1
                else:
                    break
            if 'b' not in word_list:
                break
            
        return count
        
my_object = Solution()
# print(f"nlaebolko:{my_object.maxNumberOfBalloons('nlaebolko')}")
print(f"loonbalxballpoon: {my_object.maxNumberOfBalloons('loonbalxballpoon')}")