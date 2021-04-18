class MenuItem:
    """ Model menu item """
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name = "latte", cost = 2.5, water = 200, milk = 150, coffee = 24),
            MenuItem(name = "espresso", cost = 1.5, water = 50, milk = 0, coffee = 18),
            MenuItem(name = "cappuccino", cost = 3, water = 250, milk = 50, coffee = 24)
        ]
    
    def get_items(self):
        """ Return string of menu in order like latte/espresso/cappuccino"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        """[summary]
        Args:
            order_name (string): input order name to be checked if the item exist within the MenuItem list
        Returns:
            MenuItem: return MenuItem object if the the order_name is found within the list of MenuItem
        """
        
        for item in self.menu:
            if item.name == order_name:
                return item
            
        print("Sorry item is not available\n")
        return None