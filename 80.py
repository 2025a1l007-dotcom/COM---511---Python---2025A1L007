##create a Product class with the product name, price, and quantity.Add an instance method to calculate the total cost .Take these values from the user and display the product name and total cost.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity


# Take input from the user
name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))

# Create an object
p = Product(name, price, quantity)

# Display the result
print("Product Name:", p.name)
print("Total Cost:", p.total_cost())
