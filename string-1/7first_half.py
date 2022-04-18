def first_half(str): 
    l = int(len(str)/2)
    return str[:l]

print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))