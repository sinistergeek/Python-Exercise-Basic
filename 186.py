scores = {
    'Foo':10,
    'bar':34,
    'Miu':88
        }

print(scores)

sorted_name = sorted(scores)
print(sorted_name)
for s in sorted_name:
    print("{} {}".format(s,scores[s]))

print(sorted(scores.values()))

print('')
sorted_names = sorted(scores,key=lambda x:scores[x])
for k in sorted_names:
    print("{} : {}".format(k,scores[k]))

print(' ')

sorted_names = sorted(scores,key=scores.__getitem__)
for k in sorted_names:
    print("{} : {}".format(k,scores[k]))

