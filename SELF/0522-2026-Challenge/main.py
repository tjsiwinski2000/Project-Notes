def next_word(current_word, word_list):
    return_list=[]
    for word in word_list:
        matching_letters=0
        for letter in word:
            if letter in current_word:
                matching_letters +=1
        #print(f"current_word:{current_word}, matching_letters:{matching_letters}")
        if matching_letters ==2:    
            return_list.append(word)
    return return_list
            

def word_ladder(start_word, end_word, word_list):
    """Return shortest sequence of words to get from start to end, return as list, 
    if no path exists return None."""
    
    word_list.remove(start_word)
    #housekeeping JIC start word is in the list
    
    # Only one letter at a time can be changed
    
    final_list =[] 
    # list of words that gets returned 
    impossible = False
    # fail safe to prevent infinite loop
    next_possible =[]
    # potential next words, must match two letters to current "link_word"
    current_word_chain=start_word
    
    while current_word_chain != end_word:
        next_possible =next_word(current_word_chain, word_list)
        for word in next_possible:
            for letter in word:
                if letter in end_word:
                    final_list.append(word)
                    word_list.remove(word)
                    current_word_chain = word
                    break
        print(final_list)

    return(final_list)
        
    
valid_words = {"cat", "bat", "cot", "cog", "dog", "log","pig"}

print(f"final output: {word_ladder("cat","dog",valid_words)}")