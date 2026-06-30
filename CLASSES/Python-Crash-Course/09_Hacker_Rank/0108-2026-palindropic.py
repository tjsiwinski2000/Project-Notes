for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(*[item for item in range(1,i) if item > 0], *[abs(item-i) for item in range(i+1) if item -i != 0],sep='')
# Example input 5
# Example output (note spaces need to be removed)
# 1
# 121
# 12321
# 1234321
# 123454321