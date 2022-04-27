def end_other(a,b): 
    string_a = a.lower()
    string_b = b.lower()
    

    if string_a.endswith(string_b): 
        return True 
    elif string_b.endswith(string_a): 
        return True 
    else: 
        return False 


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
