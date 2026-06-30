from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()

# with open('pi_million_digits.txt') as f1:
#     contents=f1.read
    
lines = contents.splitlines()
pi_string=''

for line in lines:
    pi_string += line.lstrip()
    
pi_string=''
#oddly path doesn't default to same location as running PY
path2 = Path('./1211-2025/pi_million_digits.txt')
contents2 = path2.read_text()
for line in contents2.splitlines():
    pi_string += line.lstrip()

if '090665' in pi_string:
    print("found 090665 in pi")

print(pi_string[:200])