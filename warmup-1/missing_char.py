def missing_char(str, n):
    front = str[:n]
    end = str[n+1:]
    return front+end

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))


