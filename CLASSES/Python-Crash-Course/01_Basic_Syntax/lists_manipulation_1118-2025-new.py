#pg124 Crash Course 
# ... while loop clever popping
unconfirmed = ['alice','brian','candace']

confirmed = []

while unconfirmed:
    current_user = unconfirmed.pop()
    print(f"verifying {current_user.title()}")
    confirmed.append(current_user)
    
print(f"Confirmed user list:{confirmed}")
print(f"Unconfirmed user list:{unconfirmed}")
print("=" *10)

letters = ['a', 'b', 'a', 'c', 'a' , 'd']
print(letters)

while 'a' in letters:
    letters.remove('a')
print(letters)

print("*" *10)
sandwhich_orders = ['tuna', 'ham', 'liverwurst', 'monkey-meat']
sandwhiches_completed =[]

while sandwhich_orders:
    next_sandwhich = sandwhich_orders.pop()
    print(f"Working on your {next_sandwhich}")
    sandwhiches_completed.append(next_sandwhich)
print(f"completed sandwhiches {sandwhiches_completed}")
print(f"current orders not completed{sandwhich_orders}")