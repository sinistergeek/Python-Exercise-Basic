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
