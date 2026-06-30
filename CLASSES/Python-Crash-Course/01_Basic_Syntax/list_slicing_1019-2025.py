
# creating a separate list via slicing
my_teams = ['knicks', 'mets', 'giants']
klif_teams = my_teams[:]
klif_teams.append('tigers')

print(f"my_teams: {my_teams}")
print(f"klif_teams: {klif_teams}")

print("=" * 40 )

 # creates a second pointer to same list()
my_teams = ['knicks', 'mets', 'giants']
klif_teams = my_teams
print(f"my_teams: {my_teams}")
print(f"klif_teams: {klif_teams}")

# test list of 9 numbers
my_list= list(range(1,10))
print(my_list)
# first three items
print(my_list[:3])
# middle three items
s=int(len(my_list)/3)
print(my_list[s:6])
# last three items
print(my_list[6:])
