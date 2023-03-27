def twelve_days_of_christmas(n):
    days = ["A partridge in a pear tree",
            "Two turtle-doves, and",
            "Three French hens",
            "Four calling birds",
            "Five golden rings",
            "Six geese a laying",
            "Seven swans a swimming",
            "Eight maids a milking",
            "Nine ladies dancing",
            "Ten lords a leaping",
            "Eleven pipers piping",
            "Twelve drummers drumming"]

     # Create a new list with the first n elements of the days list
    d = days[:n]

    # If the list is empty, do nothing
    if len(d) == 0:
        pass
    else: 
        print(d[-1])
        d.pop()
        return twelve_days_of_christmas(n-1)
    # Otherwise, print the last element of the list and recursively call the function with n-1
        
        

twelve_days_of_christmas(5)
print()
twelve_days_of_christmas(12)
print()
twelve_days_of_christmas(13)
print()
twelve_days_of_christmas(20) # it prints the last element multiple times until n is reduced to the expected value of at least 12 or lower
print()
twelve_days_of_christmas(0) # calling it with 0 will return nothing
print()
twelve_days_of_christmas(-1) # calling it with a negative value will make n access the list backwards
