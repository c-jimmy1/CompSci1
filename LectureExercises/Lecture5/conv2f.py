def convert2fahren(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("0 ->", convert2fahren(0))
print("32 ->", convert2fahren(32))
print("100 ->", convert2fahren(100))