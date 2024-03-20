collection = list()
for datum in data_set:
    if condition(datum):
        collection.append(datum)
    else:
        new = modify(datum)
        collection.append(new)

collection = [d if condition(d) else modify(d) for d in data_set]
