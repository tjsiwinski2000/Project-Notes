# 0617-2026
# working thr. idea from AI on solving problem with array of numbers


def left(list,tgt):
    for index in range(0,len(list)):
        if list[index] == tgt:
            return index
    return -1

def right(list,tgt):
    for index in range(len(list)-1, 0,-1):
        if list[index] == tgt:
            return index
    return -1

nums = [5,7,7,8,8,10]
target = 8

print(f'{left(nums,target)},{right(nums,target)}')
