from pathlib import Path

path = Path('./1211-2025/Frankenstein.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass#print(f"Sorry, the file {path} DNE")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words")

    unique_words_set = set(words)
    unique_words_list = list((unique_words_set))
    print(unique_words_list)
    print(len(unique_words_list))

    for unique_word in unique_words_list:
        count = 0
        for word in words:
            if word.lower() == unique_word.lower():
                count +=1
        print(unique_word,count)
        print('-' * 20)
    # count =0
    # for word in words:
    #     if word.lower() == 'the':
    #         count +=1
            
    # print(f"Count of 'the' : {count}")