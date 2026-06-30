for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(*[item for item in range(i+1) if item !=0], *[abs(item-i-1) for item in range(i) if abs(item -i-1) != 0],sep='')
# Example input 5
# Example output (note spaces need to be removed)
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 