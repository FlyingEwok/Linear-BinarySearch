tutlist = ["t", "u", "t", "o", "r", "i", "a", "l", "o"]

# Create global linear search function
def search(list, listlength, value): 
    counter = 0
    results = []

    for i in range (tutlistlength): 
        if (tutlist[i] == value): 
            results.append(counter)
            counter += 1
        else:
            counter += 1

    if (results == []):
        return -1     
    else:
        return results 
    
 

# intialise variables
tutlistlength = len(tutlist)
value = input("Enter a letter: ")
amount = 0

# calculate results
result = search(tutlist, tutlistlength, value)

# Find the amount of that character
if (result != -1):
    amount = len(result)

# Print the results with statement
if(result == -1): 
    print("Element is not in list") 
else: 
    print("Element is at index", result, "and there are", amount, "of those values")