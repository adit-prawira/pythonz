class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0
    
    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}\n")
    def process_coins(self):
        print("Please enter coins")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"Enter number of {coin}: "))*self.COIN_VALUES[coin]
        return self.money_received
    def make_payment(self, cost):
        """Return boolean value to will check of whether or not the payment has been successfully made
        Args:
            cost (float): cost of the drink
        """
        
        # process coins first to make sure if customer using coins or not
        self.process_coins()
        if self.money_received >= cost:
            change = round(money_received - cost, 2) # round to 2 significant figures
            print(f"Transaction status: Completed\nChange: {self.CURRENCY}{change}\n")
            self.profit += cost
            self.money_received = 0
            return True
        self.money_received = 0
        print("Transaction status: Failed\n Money is refunded\n")
        return False