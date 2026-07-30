# The challenge: Write a function that checks whether a given list of numbers is sorted in either ascending or descending order.
def check_sort(in_list):
    in_list_lengh = len(in_list)
    status=""
    for count in range(0, in_list_lengh-1):
        if in_list[count] > in_list [count+1]:
            status += "D"
        elif in_list[count] < in_list [count+1]:
            status += "A"
    
    if 'A' in status and 'D' in status:
        return "Not Sorted"
    elif 'A' in status:
        return "Sorted Ascending"
    else:
        return "Sorted Descending"
    


print(check_sort([1,2,2,3,4]))