"""Practice with Dictionaries and For Loops"""

in_stock: dict[str, bool] = {"carrots": True, "Beets": False, "Apples": True}

# print out the keys that have True values
for key in in_stock:
    # key is going to be "Carrots", "Beets", and "Apples"
    # in_stock[key] is going to be True, False, True
    if in_stock[key]: # if in_stock[key] is True
        print(key)