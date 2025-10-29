def fibonacci_list(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n):
        next_num = fib_list[i-2] + fib_list[i-1]
        fib_list.append(next_num)
    
    return fib_list

def fibonacci_num(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a,b = 0,1
    for _ in range(2, n+1):
        a,b = b, a+b
    return b

print("fibonacci list: ", fibonacci_list(13))
print("fibonacci number: ", fibonacci_num(13))