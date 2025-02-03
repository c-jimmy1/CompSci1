values = [ 14, 10, 8, 19, 7, 13 ]

val_1 = input("Enter a value: ").strip()
print(val_1)
val_1 = int(val_1)
values.append(val_1)

val_2 = input("Enter another value: ").strip()
print(val_2)
val_2 = int(val_2)
values.insert(2, val_2)

print(values[3], values[-1])

print("Difference:", max(values) - min(values))
print("Average: {:.1f}".format(sum(values) / len(values)))
values.sort()
mid = len(values) // 2
median = (values[mid] + values[mid-1]) / 2
print("Median: {:.1f}".format(median))