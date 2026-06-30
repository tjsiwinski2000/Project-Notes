#flatten list w/o and built in libraries

nested = [1, [2, 3], [4, [5, [6]]]]
#return [1, 2, 3, 4, 5, 6]

def flatten(in_list):
    out_list=""
    for item in in_list:
        if type(item) == int:
            out_list += "," + str(item)
        else:
           out_list += flatten(item)
    
    return(out_list)
            
temp=flatten(nested)
print([int(n) for n in temp.lstrip(",").split(',')])
#claude feedback on flatten (above)
# Fragility:
# Only handles int — breaks with floats, strings, or mixed types
# The leading comma requires the lstrip cleanup hack
# "," + str(item) at the start produces ",1,2,3" so the strip is always needed
# ==============================================================
#claude solution 
def flatten2(in_list):
    out_list = []
    for item in in_list:
        if isinstance(item, list):
            out_list += flatten2(item)  # recursive case
        else:
            out_list.append(item)      # base case
    return out_list

nested = [1, [2, 3], [4, [5, [6]]]]
print(flatten2(nested))  # [1, 2, 3, 4, 5, 6]