print("\n----------Welcome to The Restaurant---------")

class Restaurant:

    def run(self):
        while True:
            print("\n--- Restaurant Management System ---")
            print("1. Dining")
            print("2. Takeaway")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                self.display_menu1()
                self.display_d_order()
            elif choice == '2':
                self.display_menu2()
                self.display_t_order()
                break
            else:
                print("Invalid choice. Please try again.")

#===============================================================================================================

    def __init__(self):
        self.dMenu = {
            'Pizza': 100,
            'Burger': 150,
            'Pasta': 120,
            'Dessert': 50,
            'Cold Coffee': 50,
            'Hot Coffee': 100,
            'Soda': 60,
            'Frappuccino': 150,
            'Teapot': 200,
            'Bagel': 75,
            'Pasta Salad': 100,
            'Garlic Bread': 200,
            'Cheese Burger': 10,
            'Tomato Soup': 50,
            'Vegetable Stir-fry': 80,
            'Fried Chicken': 120,
            'Steak': 200,
            'Chicken Nuggets': 100,
            'Fish and Chips': 150,
            'Spaghetti Carbonara': 150,
            'Chicken Parmesan': 100,
            'Grilled Salmon': 250,
            'Grilled Steak': 200,
            'Grilled Chicken Breast': 150,
            'Lobster Rolls': 250,
            'Tuna Salad': 200,
            'Crab Cakes': 250,
            'Lobster Bisque': 250,
            'Fried Shrimp': 200,
        }
        
        self.takeaway_menu = {
            'Pizza': 100,
            'Burger': 150,
            'Pasta': 120,
            'Dessert': 50,
            'Cold Coffee': 50,
            'Hot Coffee': 100,
            'Soda': 60,
            'Frappuccino': 150,
            'Teapot': 200,
            'Bagel': 75
        }

        self.orders = []

# =========================================================================================================================

    def display_menu1(self):
        print("Welcome to the Restaurant!")
        print("Here is our menu:")
        for item, price in self.dMenu.items():
            print(f"{item}: ${price:.2f}")

        while True:
            item = input("Please enter the item you want to order (or 'done' to finish): ").capitalize()
            if item == 'Done':
                break

            if item in self.dMenu:
                quantity = int(input(f"How many {item}s would you like to order? "))
                self.orders.append({"item": item, "quantity": quantity, "price": self.dMenu[item]})
                print(f"{quantity} {item}(s) added to your order!")
            else:
                print("Item not found in our menu.")
        print("\n================================================")

    # =============================================================================================================================

    def display_menu2(self):
        print("Welcome to the Restaurant!")
        print("Here is our menu:")
        for item, price in self.takeaway_menu.items():
            print(f"{item}: ${price:.2f}")

        while True:
            item = input("Please enter the item you want to order (or 'done' to finish): ").capitalize()
            if item == 'Done':
                break

            if item in self.takeaway_menu:
                quantity = int(input(f"How many {item}s would you like to order? "))
                self.orders.append({"item": item, "quantity": quantity, "price": self.takeaway_menu[item]})
                print(f"{quantity} {item}(s) added to your order!")
            else:
                print("Item not found in our menu.")
        print("\n=============================================")

    # ====================================================================================================

    def display_d_order(self):
        print("\nYour Dining Order:")
        total = 0
        for order in self.orders:
            print(f"{order['quantity']} x {order['item']} - ${order['price'] * order['quantity']:.2f}")
            total += order['price'] * order['quantity']
        print(f"\nTotal: ${total:.2f}")
        self.orders = []  # Clear orders after displaying the bill

    def display_t_order(self):
        print("\nYour Takeaway Order:")
        total = 0
        for order in self.orders:
            print(f"{order['quantity']} x {order['item']} - ${order['price'] * order['quantity']:.2f}")
            total += order['price'] * order['quantity']
        print(f"\nTotal: ${total:.2f}")
        self.orders = []  # Clear orders after displaying the bill

#===============================================================================================================

restaurant = Restaurant()
restaurant.run()
