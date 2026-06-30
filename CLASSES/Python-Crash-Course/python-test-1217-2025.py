#from chatgpt.com

n = int(input())
arr = list(map(int, input().split()))
#----------------------------

for _ in range(int(input())):
    s = input().strip()
#----------------------------
s='siwinski'
s[::-1]                    # reverse 'iksniwis'
s.lower(), s.upper()       # ('siwinski', 'SIWINSKI')
s.count('a')               # 0 
''.join(sorted(s))         # 'iiiknssw'

my_list=[ord(item) for item in s]
out = ''
for num in my_list:
    out += str(num)
#115105119105110115107105
#----------------------------

def is_pal(s):
    return s == s[::-1]
#----------------------------

arr.append(x)
arr.extend([1,2])
arr.pop()
arr.sort()
sorted(arr)
#----------------------------

[x*x for x in arr if x % 2 == 0]
#----------------------------

from collections import Counter

freq = Counter(arr)
most_common = freq.most_common(1)
#----------------------------

d = {}
d.get(key, 0)
#----------------------------

a & b   # intersection
a | b   # union
a - b   # difference
#----------------------------

Counter(s)
#----------------------------

seen = set()
for x in arr:
    if target - x in seen:
        return True
    seen.add(x)
#----------------------------

left = 0
for right in range(len(s)):
    while condition:
        left += 1
#----------------------------

sorted(arr, key=lambda x: (x[1], -x[0]))

#----------------------------
# second largetst number in a list 
def runner_up(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2]
