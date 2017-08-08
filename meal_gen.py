import random

entree = ["a well-done steak", "assorted vegetables", "roasted duck", "chicken parmesan"]
side = ["mashed potatoes", "green beans", "rice", "a salad"]
dessert = ["chocolate mousse", "cheesecake", "an ice cream sundae"]
drink = ["water", "soda", "juice", "tea"]

print ("Your dinner consists of " + random.choice(entree) +", "+ random.choice(side) +", "+ random.choice(dessert) +", and "+ random.choice(drink))
