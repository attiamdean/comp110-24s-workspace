"""Practice with Dictionaries"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
# adds element to dictionary
ice_cream["mint"] = 3
# takes item off dictionary
ice_cream.pop("mint")

# accessing
# this is where the single quotes on dictionary items becomes useful
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#can use subscription notation
ice_cream["vanilla"] += 1

# checking if in dictionary
print("mint" in ice_cream)
# returns false because its not
