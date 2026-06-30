#0608-2026
#
# leetcode challenge 
# [https://leetcode.com/problems/longest-common-prefix/submissions/2026572664/]
# successful submit 11:20am
# a lot of edge case required code tweaks
# edge case IMHO weren't in original probem statement
# ====================================================
# ==================================================== 
# PROBLEM STATEMENT
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
 
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            if len(strs[0]):
                return strs
            else:
                temp="\"\""
                return temp

        # find shortest word in a list
        shortest_word = min(strs,key=len)
        print(f'shortest word {shortest_word}')
        # create shallow copy of list, remove shortest word
        new_strs = strs[:]
        new_strs.remove(shortest_word)
        word_score=[]
        min_word_score=0
        
        # iterate thr. list of words, using shortest word as test
        for item in new_strs:
            print(f'evaluating {item}')
            temp =""
            temp_word_score=0
            count=0
            for letter in shortest_word:
                temp += letter
                count +=1
                if temp in item[:count]:
                    temp_word_score += 1
                    print(f'evaluating {temp} and {item} temp_word_score = {temp_word_score}')
                else:
                    word_score.append(temp_word_score)
                    print(f'word_score now {word_score}')
                    break
                # if flow and flower issue e.g. entire shortest_word matches
                if len(temp) == len(shortest_word):
                    word_score.append(temp_word_score)
                print(f'word_score now {word_score}')
        if word_score:
            min_word_score=min(word_score)   
        print(f'min_word_score = {min_word_score}')
        final_result =""
        if min_word_score > 0:
            final_result = shortest_word[:min_word_score]
                
        return final_result
                
            

# strs = ["flower","flow","flight"]
strs = ["a"]
strs=[""]
# strs=["reflower","flow","flight"]
myObj = Solution()
result=myObj.longestCommonPrefix(strs)
print(result)