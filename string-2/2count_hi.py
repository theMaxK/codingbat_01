def count_hi(str): 
    count = 0 
    for i in range(len(str)-1): 
        if str[i] == 'h'and str[i+1] == 'i': 
            count +=1 
           
    return count  
            
    # return count  

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))