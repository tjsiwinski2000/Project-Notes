from pathlib import Path

path = Path('./1211-2025/Frankenstein.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass#print(f"Sorry, the file {path} DNE")
else:
    print(f"The number of 'the' is {contents.count('the ')}")
    