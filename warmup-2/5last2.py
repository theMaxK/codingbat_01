def last2(str): 
    last_2 = str[len(str)-2:]
    count = 0 

    for i in range (len(str)-2): 
        sub = str[i:i+2]
        if sub == last_2: 
            count = count + 1
    return count  

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
