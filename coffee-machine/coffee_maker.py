class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        
    def report(self):
        print(f"Water: {self.resources['water']}ml\n")
        print(f"Milk: {self.resources['milk']}ml\n")
        print(f"Coffee: {self.resources['coffee']}g\n")

    def is_resource_sufficient(self, drink):
        """[summary]

        Args:
            drink (MenuItem): the existing item in the MenuItem that would be created

        Returns:
            Boolean: the value will determine whether or not the resources is enough to make the order
        """
        is_sufficient = True
        for item in drink.ingredients:
            # item will be the key of the dict
            # value of the resources if below of what has been stated in the menu
            if(drink.ingredients[item] > self.resources[item]):
                print(f"Sorry the resources is not enough to make {drink.name}\n")
                is_sufficient = False
        return is_sufficient

    def make_coffee(self, order):
        """[summary]
        Args:
            order (MenuItem): this object will be utilized to deduct the existing resources
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Your {order.name} has been made")