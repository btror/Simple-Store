from Services import Services

items = {}
totalCost = 0
continueShopping = ''

while True:
    item = input("What do you want to buy?")
    price = Services().userNumber("What is the price of the " + item + "?")
    amountOfItems = Services().userNumber("How many " + item + "'s do you want to purchase?")
    continueShopping = Services().decision("Continue shopping? Type 'yes' or 'no'.")
    cart = Services().addItems(price, amountOfItems)
    items[item] = cart
    if continueShopping != "yes":
        break
    else:
        totalCost = Services().calculatePrice(items)
        print("The total so far is:", totalCost)

totalCost = Services().calculatePrice(items)
print("The total for all items is", totalCost)