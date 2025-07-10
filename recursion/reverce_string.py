# Programm for string reverce

def reverce_string(str_r):
    if not str_r:
        return str_r
    str_r = reverce_string(str_r[1:]) + str_r[0]
    return str_r

str_r = "hello"
print(reverce_string(str_r))
    
