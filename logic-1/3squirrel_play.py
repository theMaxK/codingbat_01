def squirrel_play(temp, is_summer):
    if temp >=60 and temp <=90: 
        return True 
    elif is_summer == True: 
        if temp >=60 and temp <=100:
            return True 
        else: 
            return False 
    else: 
        return False 



    

print(squirrel_play(70,False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))


