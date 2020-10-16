tutlist = ["t", "u", "t", "o", "r", "i", "a", "l", "o"]

# Create search function
def search(list, listlength, value, amount): 
  
    for i in range (tutlistlength): 
        if (tutlist[i] == value): 
            amount += 1
            return i 
    return -1 

def search2(list, listlength, value, amount):
    if (amount > 1):
        for i in range (tutlistlength): 
            if (tutlist[i] == value): 
                amount += 1
                return i 
        return -1 
  

# intialise variables
tutlistlength = len(tutlist)
value = input("Enter a letter: ")
amount = 0

result = search(tutlist, tutlistlength, value, amount) 
if(result == -1): 
    print("Element is not in list") 
else: 
    print("Element is at index", result, "and there are", amount, "of those values")