for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(str([item for item in range(1,i) if item > 0]).replace(' ','').replace(',','').replace('[','').replace(']',''),str([abs(item-i) for item in range(i+1) if item -i != 0]).replace(' ','').replace(',','').replace('[','').replace(']',''))
# Example input 5
# Example output (note spaces need to be removed)
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1