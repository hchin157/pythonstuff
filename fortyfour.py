#The next batch of code can ask for input and sort a given list.
print("-------------------------------------------------")
print("If you type letters, the program will break. :(")
print("-------------------------------------------------")

list = []

def choose():
    value = input("~ How many numbers would you like to sort? ")
    n = int(value)
    for x in range (n):
        num = input("~ Please enter number: ")
        number = int(num)
        list.append(number)

def swap():
    for i in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list[i + 1]:
                n = list[i+1]
                list[i + 1] = list[i]
                list[i] = n
choose()
swap()
print(list)
