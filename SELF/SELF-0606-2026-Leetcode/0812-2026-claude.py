# Write a function that compresses a string using run-length encoding — consecutive repeated characters get collapsed into the character followed by its count.
# "aaabbc" -> "a3b2c1"
# "abcd"   -> "a1b1c1d1"


def compress(s):
    # accomodate "aaaa" = a4
    if len(set(s)) ==1:
        return s[0] + str(len(s))
    # otherwise 
    len_s = len(s)
    bypass =0
    out_string=''
    for index in range(0,len_s):
        if index >= bypass:
            repeats =1
            current = s[index]
            if index == len_s-1:
                out_string += f'{s[index]}{repeats}'
                return(out_string)
                
            next = s[index+1]
            while current == next:
                
                current = s[index + repeats]
                next = s[index + repeats + 1]
                repeats +=1
            out_string += f'{s[index]}{repeats}'
            bypass = index + repeats 
    return(out_string)


print(compress('aaaa'))