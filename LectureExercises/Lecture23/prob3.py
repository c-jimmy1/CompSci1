
def fib(n):
    # NON RECURSIVE
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
