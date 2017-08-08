#This takes a pre-programmed list and attempts to find a specific value in the list.
#This required a lot of help from the Internet...

list = [1, 5, 12, 17, 34, 68, 99]

def findnum(someList, y):
    if len(someList) == 0:
        return False
    else:
        mid = len(someList)//2
        if y == someList[mid]:
            return True
        else:
            if y > someList[mid]:
                return findnum(someList[mid + 1], y)
            else:
                return findnum(someList[:mid], y)

print (findnum(list, 6))
