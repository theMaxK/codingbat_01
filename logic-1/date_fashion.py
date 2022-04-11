def date_fashion(you, date): 
    if you >= 8: 
        if date <= 2: 
            return 0 
        else: 
            return 2
    elif date >= 8: 
        if you <= 2: 
            return 0 
        else: 
            return 2
    elif you <= 2: 
        return 0 
    elif date <= 2: 
        return 0 
    else: 
        return 1

print(date_fashion(5, 10))
print(date_fashion(5, 2))
print(date_fashion(5, 5))