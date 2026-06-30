# Example 1:
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

# Example 2:
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

# Example 3:
# Input: s = "abc"
# Output: 1


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if 'a' in s[i:j] and 'b' in s[i:j] and 'c' in s[i:j]]
        # count=0
        #for substring in substrings:
            # if 'a' in substring and 'b' in substring and 'c' in substring:
            #     count += 1
            #     print(f'{count} abc in {substring}')
        # match= [item for item in substrings if 'a' in item and 'b' in item and 'c' in item]  
        return len(substrings)
                
            
my_object = Solution()
print(my_object.numberOfSubstrings('abcabc'))
 