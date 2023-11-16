lines = ['grape banana mango',
         'nut orange peach',
         'apple nut banana apple mange']

one_line = ' '.join(lines)
print(one_line)

fruits = one_line.split()
print(fruits)

unique_fruits =[]
for word in fruits:
    print("word: ",word)
    if word not in unique_fruits:
        print("uniq: ",unique_fruits)
        unique_fruits.append(word)
print(sorted(unique_fruits))

unique = sorted(set(fruits))
print(unique)
