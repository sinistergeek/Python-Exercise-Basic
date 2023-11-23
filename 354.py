text = ['aaaa','bb','cc ccc']

length_1 = map(lambda x: len(x),text)
print(length_1)
print(list(length_1))

length_2 = map(len,text)
print(length_2)
print(list(length_2))
length_3 = [len(s) for s in text]
print(length_3)
