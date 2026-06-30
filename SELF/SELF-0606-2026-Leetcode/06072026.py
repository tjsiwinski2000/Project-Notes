def proof_concept(in_string):
    count = len(in_string)
    for loop_counter in range(0,count):
        print(f'{loop_counter}. {in_string[loop_counter]}')


s = "abcabcbb"
proof_concept(s)