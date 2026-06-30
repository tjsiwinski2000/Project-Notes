# there was some wierdness with this, mabye file wasn't fully copied over 
from pathlib import Path

path = Path('pi_digits.txt')
# remove white space at EOL
contents = path.read_text().rstrip()

# splitlines returs [] of all lines in a file 
lines = contents.splitlines()
print(f"lines is a {type(lines) }")
for line in lines:
    print(line)
    
pi_string =''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))
print(pi_string[:15])
