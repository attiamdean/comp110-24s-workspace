"""Practice instantiating pizza class"""

from pizza import Pizza

# wont actually have to call stuff like this, just to demonstrate
my_pizza: Pizza = Pizza()
my_pizza.size = "large"
my_pizza.toppings = 1
my_pizza.gluten_free = True

print(Pizza) # wont print because it is a class
print(my_pizza) # gives that it is an object in a location in memory
print(my_pizza.size) #

# when you have the __init__ variable: 
a_pizza: Pizza = Pizza("large", 1, True) #same as my_pizza above
print(a_pizza.size) # prints "large"

sals_pizza: Pizza = Pizza("small", 2, False)

def price(pizza_order: Pizza) -> float:
    """Calculate and return cost of pizza"""
    cost: float = 0.0
    if pizza_order.size == "large":
        cost = 6.0
    else: 
        cost = 5.0
    # charge .75 per topping
    cost += .75 * pizza_order.toppings
    # charge $1 for gluten free 
    if pizza_order.gluten_free == True:
        cost += 1.0
    return cost

print(price(my_pizza)) # prints the price
print(sals_pizza.price()) 