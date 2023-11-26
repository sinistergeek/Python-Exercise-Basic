def create_bank(n=0):
    balance = n
    def bnk(change=0,prev=False):
        nonlocal balance
        prev_balance = balance
        balance += change
        if prev:
            return prev_balance
        else:
            return balance
    return bnk

bank = create_bank(20)
print(bank())
print(bank(7))
print(bank(10,prev=True))
print(bank())
