import random
import dice_faces

def dice_throw():
    roll1 = str(random.randint(1,6))
    temp= dice_faces.dice_dict.get(roll1) 
    return temp

print(dice_throw())
print(dice_throw())
