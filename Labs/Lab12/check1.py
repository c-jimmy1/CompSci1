def add(m: int, n: int) -> int:
    if n == 0:
        return m
    elif n > 0:
        return add(m + 1, n - 1)
    else:
        return add(m - 1, n + 1)


def mult(m: int, n: int) -> int:
    if n == 0:
        return 0
    elif n > 0:
        return add(m, mult(m, n - 1))
    else:
        return -mult(m, -n)



def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return mult(x, power(x, n - 1))

if __name__ == "__main__":
    print("add(5, 3)  =>", add(5, 3))         # 8
    print("mult(8, 3) =>", mult(8, 3))        # 24
    print("power(6, 3) =>", power(6, 3))      # 216