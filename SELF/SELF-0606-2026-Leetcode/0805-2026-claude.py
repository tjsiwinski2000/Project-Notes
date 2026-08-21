#Write a function second_largest(nums) that returns the second-largest unique value in a list of numbers.

def second_largest(nums):
    try:
        temp = sorted(list(set(nums)))[-2]
    except IndexError:
        return None
    return temp

print(second_largest([1,5,5,4,5]))

