alien_0 = {
    'color' : 'green',
    'points' : 5
}

#all
print(alien_0)

#green
print(alien_0['color'])

#5
print(alien_0['points'])

#adding new key-value pair
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)

#removing a KV pair, once deleted gone FOREVER
del alien_0['points']
print(alien_0)