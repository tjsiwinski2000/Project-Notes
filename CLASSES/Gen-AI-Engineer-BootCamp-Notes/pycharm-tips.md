## running the code  ##
...CLASSES\PycharmProjects\Gen_AI_Engineer..\lesson1\task1

PYCHARM TIP see variables in console.
green ▶ Run button, it opens a Run panel
- not the interactive Console 
— and it won't populate variables unless debugging

### Loading environment variables ###
from dotenv import load_dotenv
load_dotenv()

-or-
import os
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

### Run Code in Console ###
- Select All Text (Cntrl A)
- "Execute selection in console" (Alt+Shift+E) 
- RESULT: send lines from your editor into the console


### working with console ###
console change working directory
os.chdir(r"C:\..\Gen_AI_Engineer_..\lesson0\task1")
os.cwd()
os.listdir()
['main.py', 'main_real.py', 'task-info.yaml', 'task-remote-info.yaml', 'task.md']

import sys
sys.path.append('.')
- above needed to find main_real, despite navigating to its location
import main_real

### working with console STOP CACHING ###
import main_real
- has to be done every time you edit main_real
- testing at console level
HOW TO STOP caching which is a common problem
import importlib
import main_real
importlib.reload(main_real)

### settings ###
In PyCharm: Settings/Preferences → Editor → Color Scheme → Python, 
then find Line Comment (and Block Comment if you use """..."""-style ones) in the list, 
click the color swatch, and pick whatever color you want.

Cntrl+Alt+S