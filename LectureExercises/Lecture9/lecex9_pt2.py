census = [340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082,
          5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782,
          8236, 17558, 17990, 18976, 19378]

i = 0
total_pct_change = 0.0
while i < len(census) - 1:
    pct_change = (census[i + 1] - census[i]) / census[i] * 100
    total_pct_change += pct_change
    i += 1

average_pct_change = total_pct_change / (len(census) - 1)

print(f"Average = {average_pct_change:.1f}%")
