i=0
def display_info(company,**kwargs):
    print(f'Company name: {company}')
    if i == 0:
        
        if 'price' in kwargs:
            print(f"Price: ${kwargs['price']}")
        else:
            print("Enter the price")
            a = int(input())
            if a > 0:
                display_info(company='SD POR',price=a)
            else:
                print("***** +ve ++++++++++")


display_info(company='CD Project')
