words = []
keys = input('Enter Words \n')
user_words = keys.split()
#[item.lower() for item in user_words]
words.append(keys.lower())
for i in words:
    j = i.replace(' ','')
#print("".join(words))
print(j)
