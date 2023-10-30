class Table:
    total_tables = 0
    
    def __init__(self,wood_used,year):
        self.wood_used = wood_used
        self.year = year
        Table.total_tables = Table.total_tables + 1
        print('Table made in {} wood has been created.'.format(self.wood_used))

    def setGuarantee(self,guarantee):
        self.guarantee = 25

t1 = Table('Ebony',2020)
print(t1.__dict__)
print("Attributes before calling setGaurantee() method.",t1.__dict__)
t1.setGuarantee(25)
print("Attributes after calling setGaurantee() method.",t1.__dict__)
