seed = input("please enter seed")
print(f"You entered {seed}")
shift_amount= +2
encoded_chars = []
for char in seed:
    original_ascii = ord(char)
    shifted_ascii = original_ascii + shift_amount
    shifted_char = chr(shifted_ascii)
    encoded_chars.append(shifted_char)

result_string = "".join(encoded_chars)
print(result_string)


