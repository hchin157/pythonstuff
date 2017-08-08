dict =  {"6-pound Pekin duck": "1", "kosher salt": "3 tablespoons", "5-spice powder": "1 tablespoon", "large orange zested and cut into 6 wedges": "1", "grated ginger": "1 tablespoon ", "grated garlic": "1 tablespoon"}
lst = ["Step 1", "step 2", "step3", "step4"]
#gll =  ["2 cups orange juice", "1 tablespoon honey", "2 tablespoons sugar", "2 tablespoons soy sauce", "1 2-inch piece of ginger, thickly sliced", "3 star anise"]

# for item in lst:
#     print(item)

def cookbook():
    print ("------------")
    recipe = input("What would you like to cook today?")
    if recipe == 'glazed duck':
        print ("Sounds good!")
        for n in dict:
            print (dict.keys()[0])
            print (dict.values()[0])
    else:
        print ("Sorry, I don't know that one.")
        cookbook()

cookbook()
