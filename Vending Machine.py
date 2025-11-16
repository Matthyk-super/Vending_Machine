class Beverage:
   def __init__(self, name, price):
       self.name = name
       self.price = price
       self.stock = 10

   def __str__(self):
       return (self.name + " - $" + str(round(self.price, 2)) +
                " (" + str(self.stock) + " left)")

# The 6 beverages
class VendingMachine:
   def __init__(self):
       self.beverages = [
           Beverage("Coke", 2.85),
           Beverage("Orange Fanta", 2.85),
           Beverage("Sprite", 2.85),
           Beverage("Apple Juice", 3.15),
           Beverage("Lemonade", 2.85),
           Beverage("Water", 2.65)
       ]

   def display_menu(self):
# Using enumerate starting in the position 1 to get the option number and beverage name (e.g. 1 coke, 2 Orange Fanta)
       for i, bev in enumerate(self.beverages, 1):
           print(str(i) + ". " + str(bev))

# If user puts in anything but a positive number
   def get_valid_integer(self, prompt):
       user_input = input(prompt)
       if user_input.strip().isdigit():
# Removing leading and trailing spaces using strip()
           return int(user_input.strip())
       print("Invalid choice. Try again.")
       return self.get_valid_integer(prompt)

# If the money is not valid
   def get_valid_float(self, prompt):
       user_input = input(prompt)
# Removing the decimal point, and validating that the input is a digit
       if user_input.replace('.', '', 1).isdigit():
           return float(user_input)
       print("Invalid amount. Please insert cash or card.")
       return self.get_valid_float(prompt)

# The prompt
   def select_beverage(self):
       choice = self.get_valid_integer("\n" "Select a beverage (1-6): ")

# If a beverage is out
       if 1 <= choice <= len(self.beverages):
           selected = self.beverages[choice - 1]
           if selected.stock == 0:
               print("Sorry, " + selected.name + " is out of stock.")
# Calling back the select_beverage, to ask for another selection
               return self.select_beverage()
           return selected

# If user does not put 1-6
       print("Please select an item from the machine.")
       return self.select_beverage()

# When chosen something
   def process_payment(self, beverage):
       total_inserted = 0.0
       print("\n" + beverage.name + " costs $" + str(round(beverage.price, 2)) + ".")

# Asking for payment
       while total_inserted < beverage.price:
           remaining = round(beverage.price - total_inserted, 2)
           money = self.get_valid_float("Insert money ($" + str(remaining) + " remaining): $")
# Checking if the inserted money is greater then 0
           if money <= 0:
               print("Please insert a valid amount of money.")
           total_inserted += money
           print("Total inserted: $" + str(round(total_inserted, 2)))

       change = round(total_inserted - beverage.price, 2)
# If user input is more than the cost of the beverage, returning the change
       if change > 0:
           print("Returning change: $" + str(change))

# Getting the drink
       beverage.stock -= 1
       print("Dispensing " + beverage.name + ". Thank you and enjoy!\n")

# Keeping on going
   def run(self):
       running = True
       while running:
           self.display_menu()
           beverage = self.select_beverage()
           self.process_payment(beverage)

# Run the program
if __name__ == "__main__":
   machine = VendingMachine()
   machine.run()