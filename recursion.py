def recursion(n):
    if n < 1:
        return n
    
    print(n)
    return recursion(n - 1)

recursion(2)

def recursion(n):
    if n < 1:
        return 
    
    print(n)
    return recursion(n - 1)

recursion(2)

def a(n):
    if n > 0:
        print(f"Inside a {n}")
        return b(n - 1)
    
    if n < 1:
        return n
    else:
        print(f"Inside a {n}")
        return b(n - 1)

def b(n):
    if n > 0:
        print(f"Inside b {n}")
        return a(n - 1)
    
a(5)

# tail recursion
def rec(n):
    if n < 1:
        return n
    
    print(n)
    return rec(n - 1)

rec(2)

#head recursion
def head(n):
    if n < 1:
        return n
    
    head(n - 1)
    print(n)
    
head(5)