largest = None

for value in [-3, -41, -12, -9, -74, -15, 0] :
    if largest is None :
        largest = value
    elif value > largest :
        largest = value
    print(largest)