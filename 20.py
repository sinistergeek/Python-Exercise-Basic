def products(prod_name,price,**kwargs):
    """Assigning an arbitrary  number of keyword argumnets to a function"""
    print("Product name:",prod_name,"|Price:",price)
    print("Description:",kwargs)

products("Cup","$10",color="Red",manufacturer="ABC co.")
products("Plate","$5",material="China ceramic",size="Family size")
products("Cuttlery","$25",set_no="P5656",spoons = 12, forks=12,knives=2)
