if __name__ == '__main__':
    first_line = int(input())
    second_line = int(input())
a = '\u00b0' #degree symbol

import math
angle_rad = math.atan(first_line/second_line)
angle_deg = math.degrees(angle_rad)
angle_deg= int(round(angle_deg,0))
print(f"{angle_deg}{a}")
#✅success !