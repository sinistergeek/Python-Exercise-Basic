str = "JavaScript"
print(str.find("v"))

import re
pattern = re.compile(r'\d+')
list = pattern.findall('ok23vary168good33',0,30)
print(list)

def make_pizza(*toppings):
    """Print the list toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
