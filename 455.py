class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


for attr,value in OnlineShop.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

