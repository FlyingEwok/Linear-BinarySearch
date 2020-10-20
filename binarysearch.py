def binarySearch (list, l, listLength, value):
    # Set up mid point variable
    if listLength >= l: 
  
        midPoint = l + (listLength - l) // 2
  
        if list[midPoint] == value: # return the midpoint if the value is midpoint
            return midPoint 
        elif list[midPoint] > value: # Do a search to the left of midpoint for value then return that 
            return binarySearch(list, l, midPoint-1, value) 
        else: # Do a search to the right of midpoint for value then return that
            return binarySearch(list, midPoint + 1, listLength, value) 
    else: # if value not in list then return -1
        return -1

searchList = [1, 2, 3, 4, 5, 6, 7, 8, 99]

# Ask user for a number
try:
    value = int(input("Enter a number: "))
    # perform the binary search on the search list
    result = binarySearch(searchList, 0, len(searchList)-1, value)

    # Print the results in a statement
    if result != -1: 
        print ("Element is at index", result) 
    else: 
        print ("Element is not in list") 

except ValueError:
    print("That's no number! Try again.")    





