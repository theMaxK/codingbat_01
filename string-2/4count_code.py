def count_hi(str): 
    count = 0 
    for i in range(len(str)-3): 
        if str[i] == 'c'and str[i+1] == 'o' and str[i+3]=='e': 
            count +=1 
           
    return count  
            
    # return count  

print(count_hi('aaacodebbb'))
print(count_hi('codexxcode'))
print(count_hi('cozexxcope'))