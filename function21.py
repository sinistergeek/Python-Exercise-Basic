class Table:
    total_tables = 0

    def __init__(self,wood_used, year):
        self.wood_used = wood_used
        self.year = year
        Table.total_tables = Table.total_tables + 1
        print('Table No. {} : Table made of {} wood has been created.'.format(Table.total_tables,self.wood_used))
    def setGuarantee(self,guarantee):
        self.guarantee = guarantee

t1 = Table('Ebony',2020)
t2 = Table('Teak',2017)
t3 = Table('Mango wood',2018)
