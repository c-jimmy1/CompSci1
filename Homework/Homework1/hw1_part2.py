minute = int(input("Minutes ==> ").strip())
print(minute)

second = int(input("Seconds ==> ").strip())
print(second)

mile = input("Miles ==> ").strip()
print(mile)
mile = float(mile)
target_miles = input("Target Miles ==> ").strip()
print(target_miles)
target_miles = float(target_miles)

total_min = float((second/60) + minute)
pace_min = int(total_min/mile)
pace_sec = int(((total_min/mile) - pace_min) * 60)

speed = (mile / (total_min / 60))

target_min = int((target_miles/speed) * 60)
target_sec = int(((target_miles/speed * 60) - target_min) * 60)

print("Pace is", pace_min, "minutes and", pace_sec, "seconds per mile.")
print("Speed is {:.2f}".format(speed), "miles per hour.")
print("Time to run the target distance of {:.2f}".format(target_miles), "miles is", target_min, "minutes", "and", target_sec, "seconds.")