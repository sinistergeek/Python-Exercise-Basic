def apply_discount(product,discount):
    price = int(product['price'] * (1.0 - discount)) 
    assert 0 <= price <= product['price']
    return price


if cond == 'x':
    do_x()

elif cond == 'y':
    do_y()
else:
    assert False,(
'This should never happen, but it does '
'occassionally. We are currently trying to figure out why. Email dbadder is if you encounter this in the wild. Thanks'
            )

def delete_product(prod_id,user):
    assert user.is_admin(),'Must be admin'
    assert store.has_product(prod_id),'Unknown product'
    store.get_product(prod_id).delete()

class Indenter:
    def __init__(self):
        self.level = 0
    def __enter__(self):
        self.level += 1
        return self 
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.level -= 1
    def print(self,text):
        print('     '*self.level + text)
