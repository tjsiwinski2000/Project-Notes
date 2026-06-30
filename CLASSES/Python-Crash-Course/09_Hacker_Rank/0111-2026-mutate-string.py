def mutate_string(string, position, character):
    # print(string)
    # print(str(position))
    # print(character)
    out_value = string[:position-1] + character + string[position+1:]
    # print(out_value)
    return(out_value)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)