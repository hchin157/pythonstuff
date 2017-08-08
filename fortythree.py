list = [5, 4, 3, 2, 1]
def swap():
    for i in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list[i + 1]:
                n = list[i+1]
                list[i + 1] = list[i]
                list[i] = n

swap()
print(list)
#This is old code that sorted a list already programmed.
