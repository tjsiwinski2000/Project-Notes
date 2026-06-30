# Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
# Output: ["word","note","wood"]
# Explanation:
# - Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
# - Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
# - It would take more than 2 edits for "ants" to equal a dictionary word.
# - "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
# Thus, we return ["word","note","wood"].

#0630-2026
# successfully completed, needed one line from claude
# had some issues 
# - 1. order of returned list needs to match input
# - 2. nested for for loops 
# ----match:[break from inner] 
# ----no match:[remove after for loop exhausted ]
import copy
class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        out = copy.deepcopy(queries)
        
        for word in queries:
            for entry in dictionary:
                matches =[]
                keep = False
                #mine->matches =  [letter for letter in word if word.find(letter) == entry.find(letter)]
                # claude below accounts for location of letter more cleanly
                matches = [i for i in range(len(word)) if word[i] == entry[i]]
                keep = len(matches) >= len(word)-2
                if keep == True:
                    # print(f'{word} -> {entry} : {len(matches)}')
                    print(f'word: {word} is okay')
                    #break out of inner for loop; outer loop continues
                    break
            if keep == False:
                out.remove(word)
        return out
                

# for word in quer for word2 in dictionary 
# check for match [unchanged]
# check for one letter dif
# check for two letter dif
# add to output list

my_object = Solution()
print(my_object.twoEditWords(queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]))