from pathlib import Path
import json

path = Path('numbers.json')
if path.exists():
    print(f"found {path}")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)