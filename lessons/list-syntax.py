"""Demonstrate Basic List Syntax"""

#Create an empty list
grocery_list: list[str] = list() # <- constuctor 
#could also do
grocery_list: list[str] = [] # <- literal
print("Empty list: ")
print(grocery_list)

# add an item to a list: <list name>.apend(<item>)
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")

print("After adding things")
print(grocery_list)

# create a list with objects in it
grocery_list2: list[str] = ["eggs", "bacon", "flour"]
print("Already populated list")
print(grocery_list2)

grocery_list2.append("whipped cream")
print("after adding another thing")
print(grocery_list2)

#indexing
print("Printing out one item")
print(grocery_list[0])

# modifying by index
grocery_list: list[str] = ["bananas", "milk", "bread"]
grocery_list[1] = "almond milk" # <- can change things at a specific index
print(grocery_list)

# Length of a list
print("length")
print(len(grocery_list))

# remove item from a list
grocery_list.pop(1) # <- pop removes things at a specific index 
print("remove an item:")
print(grocery_list)

#lists and functions

def display(my_list: list[str]) -> None:
    print(my_list)
    
display(grocery_list)

#second practice function

def create(list_1: list[str], list_2: list[str]) -> list[str]:
    new_list: list[str] = [list_1, list_2]
    return new_list

x: str = create(grocery_list, grocery_list2)
print(x)
