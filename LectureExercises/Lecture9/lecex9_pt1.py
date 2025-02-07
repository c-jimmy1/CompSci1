n = input("Enter a positive integer: ").strip()
print(n)
n = int(n)

i = 0
while i < n:
    if i % 3 == 0:
        print(i)
    i += 1