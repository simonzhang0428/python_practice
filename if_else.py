weather = "sunny"
date = "Sun."
is_holiday = False
if weather == "sunny" and (is_holiday or date in ["Sat.", "Sun."]):
    print("Go play outside")
elif not is_holiday and date not in ["Sat.", "Sun."]:
    print("Go to work")

import sys

# keep the code below
goods = [
    {"name": "Computer", "price": 1999},
    {"name": "Mouse", "price": 10},
    {"name": "Yachts", "price": 20},
    {"name": "Airplane", "price": 998}
]


asset = int(sys.argv[1])
input_list = eval(sys.argv[2])

# write your code here
for choice in input_list:
    if choice > 4:
        print("Please re-enter")
        continue
    elif choice == 0:
        break

    good_name, good_price = goods[choice - 1]['name'], goods[choice - 1]['price']
    print(f'You want to buy: {good_name}')
    print(f'It is priced at: {good_price}')

    if good_price > asset:
        print("The balance is low, so go ahead and top up!")
        break
    else:
        asset -= good_price
        print("Purchase successful!")