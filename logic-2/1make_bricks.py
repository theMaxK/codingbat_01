def make_bricks(small,big,goal): 
    resto = goal 
    resto -= 5*min(big,goal/5)
    return resto-small <= 0 


print(make_bricks(3,1,8))
print(make_bricks(3,1,9))
print(make_bricks(3,2,10))
