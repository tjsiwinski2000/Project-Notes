# n = int(input())
# arr = map(int, input().split())
array = [1,3,6,6,5]
max = max(array)
while max in array:
    array.remove(max)

array = sorted(array)
print(array[-1])
# print(type(array))
# n = 9
# for count in range(1,n+1):
#     print(count)