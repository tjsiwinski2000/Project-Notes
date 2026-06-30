# Create a list  of identical objects
# Note: Python considers each a separate object

aliens =[]
# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow' }
    aliens.append(new_alien)
    
# How to access one of the identical objects
print(aliens[1])

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10 

# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)