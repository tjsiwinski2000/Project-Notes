# 01092026- fails for "overlapping" strings
# def count_substring(string, sub_string):
#     found=string.count(sub_string)
#     if (found == -1):
#         return 0
#     else:
#         return(found)

#✅0109-2026 
# - finds overlapping strings e.g. 'ABCDCDC' , 'CDC'
def count_substring(string,substring):
    index=-1
    count_finds = 0
    while True:       
        index = string.find(substring,index+1)
        if index == -1:
            return(count_finds)
        else:
            count_finds +=1
        #debug print(f"Found {substring} at {index}")
    return(count_finds)

s ='ABCDCDC'
t = 'ABC'
# t='ABC'

# print(count_substring(s,))
print(count_substring(s,t))

