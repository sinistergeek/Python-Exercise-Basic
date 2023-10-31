class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        str1 = 'name: '+self.name+' balance: '+self.balance+'.'
        return str1
    def __add__(self, other):
        balance = int(self.balance) + int(other.balance)
        return balance

b1 = Bank('customer1','10000')
b2 = Bank('friend', '1000')
print(b1)
print(b2)
print(b1 + b2)
