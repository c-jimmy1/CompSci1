
file = input('Data file name: ').strip()
print(file)

prefix = input('Prefix: ').strip()
print(prefix)

names = set()
for line in open(file):
    words = line.strip().split('|')
    fullname = words[0].strip().split(',')
    lastname = fullname[0]
    if not lastname in names:
        names.add(lastname)

total = 0
for x in names:
    if x.startswith(prefix) == True:
        total += 1    

print('{} last names'.format(len(names)))
print('{} start with {}'.format(total, prefix))