#p201 json.dumps() json.loads()

from pathlib import Path
import json

numbers = [2,3,5,7,11,13]
path = Path('./01_Basic_Syntax/json_1215-2025/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)