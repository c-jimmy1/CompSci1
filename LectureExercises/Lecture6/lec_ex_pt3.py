first = input("Enter the first number: ").strip()
print(first)
first = float(first)

second = input("Enter the second number: ").strip()
print(second)
second = float(second)

if first > 10 and second > 10:
    print("Both are above 10.")
elif first < 10 and second < 10:
    print("Both are below 10.")

avg = (first + second) / 2

print("{:.2f}".format(avg))