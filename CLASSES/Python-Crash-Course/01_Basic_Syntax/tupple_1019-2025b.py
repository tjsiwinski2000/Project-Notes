food_tupple =('pizza', 'eggs', 'bisuits','monkey-meat')
print(type(food_tupple)) #<class 'tupple'>

for item in food_tupple:
    print(item)


food_tupple[0] = 'pepperoni'
#TypeError: 'tuple' object does not support item assignment