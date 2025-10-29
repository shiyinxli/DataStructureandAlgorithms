def n_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("invalid n")
    elif n == 1 or n == 0:
        return 1
    else:
        return n*n_factorial(n-1)
    
x = n_factorial(13)
print(x)