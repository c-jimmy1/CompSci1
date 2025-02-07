nums = []

while True:
    num = input("Enter a value (0 to end): ").strip()
    print(num)
    num = int(num)
    if num == 0:
        break
    nums.append(num)

print("Min:", min(nums))
print("Max:", max(nums))
print("Avg: {:.1f}".format(sum(nums) / len(nums)))