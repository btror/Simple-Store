class Services:

    def __init__(self):
        self.items = {}

    def addItems(self, price, amount):
        self.items['price'] = price
        self.items['amount'] = amount
        return self.items

    def calculatePrice(self, items):
        totalPrice = 0
        for i, j in items.items():
            totalPrice += float(j['price']) * int(j['amount'])
        totalPrice = round(totalPrice, 2)
        return totalPrice

    def decision(self, answer):
        while True:
            userInput = input(answer)
            if userInput in ['yes', 'no']:
                return userInput
            print("Please type 'yes' or 'no'.")

    def userNumber(self, number):
        while True:
            try:
                userInput = float(input(number))
            except ValueError:
                print("Please enter a number value only!")
                continue
            else:
                return userInput