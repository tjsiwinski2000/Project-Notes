#clean up quotes.txt as an exercise 
# - some quotes too long
# - some quotes aren't quote
# - some quotes start with numbers
quotes_list = []
final=''
with open('quotes2.txt', 'r', encoding='utf-8') as f1:
    quotes_list = f1.readlines()

count =0
for line in quotes_list:
    count+=1
    line = line.replace('â€','').replace('”','')
    if len(line) <200 and len(line) > 40 :
        # print(f"{line} ")
        final+=line
print(final)
with open('quotes3.txt', 'w', encoding='utf-8') as f3:
     f3.write(final)