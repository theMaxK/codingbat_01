def close_far(a,b,c): 
    return (is_close(a, b) and is_far(a, b, c)) or  (is_close(a, c) and is_far(a, c, b)) 

def is_close(a,b): 
    return abs(a-b) <=1

def is_far(a,b,c): 
    return abs(a-c) >= 2 and abs(b-c)>=2 

print(close_far(1,2,10))
print(close_far(1,2,3))
print(close_far(4,1,3))

