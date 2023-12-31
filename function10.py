comparisonFunc = lambda a,b: a if a > b else b
print(comparisonFunc(10,3))


addFunc = lambda a,b: a+b
print(addFunc(5,2))


countries = ['India','Mauritius','France','Turkey','kenya','Hungary']
print(list(map(lambda x: len(x),countries)))


countries.sort(key = lambda x:x[0])
print(countries)


names = ['rRock Rock','table cup','bench top','legend and do','horse ride','car blast']
names.sort(key=lambda x:x.split()[-1])
print(names)


list1 = [(1,2),(4,1),(9,10),(13,-3)]
list1.sort(key = lambda x:x[0])
print(list1)


marks = [{'Subject':'Maths','Score':90},{'Subject':'Science','Score':100},{'Subject':'Geography','Score':83}]
print(list(sorted(marks, key = lambda x:x['Score'], reverse = True)))


list2 = ['AR-MO-UR','O-F','G-O-D']
print(list(map(lambda x: ''.join(x.split('-')),list2)))


list3 = [10,20,50,70]
list4 = [20,40,60,80]
print(list(map(lambda x,y: x+y,list3,list4)))
