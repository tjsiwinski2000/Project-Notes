def add(*args):
    print(type(args)) #tuple
    total=0
    for n in args:
        total += n
    return total

print(add(1,2,3,4,5))

#----------------------------------
def calculate(n,**kwargs):
    print(type(kwargs)) #dictionary
    final_num = n
    final_num += kwargs['add']
    final_num *= kwargs['multiply']
    return final_num

print(calculate(2,add=3, multiply=5))