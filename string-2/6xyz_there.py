def xyz_there(str):
    if str[:3] == 'xyz': 
        return True 

    for i in range(len(str)-2): 
        if str[i-1] != '.'and str[i] == 'x' and str[i+1] == 'y' and str[i+2] == 'z':
            return True 
        
    return False 


             
       

        
print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc')) 