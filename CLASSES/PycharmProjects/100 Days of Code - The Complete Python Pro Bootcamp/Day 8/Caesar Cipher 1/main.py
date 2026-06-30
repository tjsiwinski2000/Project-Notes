alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

def encrypt(orginal_text, shift_amount):
    orginal_text=str(orginal_text).lower()
    encode_output=""
    #print(orginal_text)
    s_list=list(orginal_text)
    for letter in s_list:
        pos1= alphabet.index(letter)
        new_index=pos1 +shift_amount
        if new_index > 25:
            new_index -= 25
        encode_output += alphabet[shift_amount]
    print(f"Here is the encoded result: {encode_output}")


encrypt(text,shift)