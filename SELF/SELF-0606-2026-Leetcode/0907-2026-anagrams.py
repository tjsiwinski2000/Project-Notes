# Here's one that builds on comprehension/string-manipulation practice but adds a new angle — grouping data with dictionaries:

# Challenge: Anagram Groups

# Write a function group_anagrams(words) that takes a list of strings and groups the words that are anagrams of each other.

# group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# Should return something like:
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def alpha_sort(in_string):
    return ''.join(sorted(in_string))

def group_anagrams(in_list):
    out_list=[] #output list
    alpha_list=[] #list of words but each alpha sorted e.g. cat=act
    for word in in_list:
        alpha_list.append(alpha_sort(word))
        
    for word in alpha_list:
        # print(alpha_list.count(word))
        if alpha_list.count(word) > 1:
            result = [in_list[i] for i, value in enumerate(alpha_list) if value == word]
            # result is list of anagram words e.g. eat, tea, ate
            if result not in out_list:
                out_list.append(result)
        if alpha_list.count(word) == 1:
            #find word that appears once
            for item in in_list:
                if alpha_sort(item) == word:
                    temp=[]
                    temp.append(item)
                    out_list.append(temp)
       
            
            
    return out_list

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))