def binarySearch (list, l, listLength, value):
    # Set up mid point variable
    if listLength >= l: 
  
        mid = l + (listLength - l) // 2
  
        if list[mid] == value: 
            return mid 
        elif list[mid] > value: 
            return binarySearch(list, l, mid-1, value) 
        else: 
            return binarySearch(list, mid + 1, listLength, value) 
    else: 
        return -1

searchList = [1, 2, 3, 4, 5, 6, 7, 8]
value = int(input("Enter a number: "))

result = binarySearch(searchList, 0, len(searchList)-1, value)

if result != -1: 
    print ("Element is at index", result) 
else: 
    print ("Element is not in list") 
