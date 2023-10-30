comparisonFunc = lambda a,b: a if a > b else b
print(comparisonFunc(10,3))


addFunc = lambda a,b: a+b
print(addFunc(5,2))


countries = ['India','Mauritius','France','Turkey','kenya','Hungary']
print(list(map(lambda x: len(x),countries)))
