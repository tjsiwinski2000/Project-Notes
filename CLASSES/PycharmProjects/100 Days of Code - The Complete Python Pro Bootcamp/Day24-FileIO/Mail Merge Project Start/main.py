#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Step 1. open the data file
with open(".\\Input\\Names\\invited_names.txt", "r") as names_files:
    names_invitees =names_files.readlines()

# Step 2. open sample letter
with open(".\\input\\Letters\\starting_letter.txt", "r") as file:
    model_letter = file.read()
    print(model_letter)

# Step 3. create file content
for name in names_invitees:
    clean_name =name.removesuffix('\n')
    updated_letter = model_letter.replace("[name]", clean_name)
    with open(f".\\Output\\ReadyToSend\\letter_for_{clean_name}.txt", mode = "w") as out_file:
        out_file.write(updated_letter)

