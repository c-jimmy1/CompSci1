
in_file = input("Enter the scores file: ").strip()
print(in_file)
out_file = input("Enter the output file: ").strip()
print(out_file)

f = open(in_file, "r")
s = f.read()

scores = []
for x in s.split():
    if x.strip():
        scores.append(int(x))

scores = sorted(scores)
f.close()

f = open(out_file, "w")

i = 0
while i < len(scores):
    scores[i] = int(scores[i])
    f.write("{:2d}: {:3d}\n".format(i, scores[i]))
    i += 1
