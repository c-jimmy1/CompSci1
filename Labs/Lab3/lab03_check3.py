bpop = input("Number of bunnies ==> ").strip()
print(bpop)
bpop = int(bpop)

fpop = input("Number of foxes ==> ").strip()
print(fpop)
fpop = int(fpop)

print("Year 1: {0} bunnies and {1} foxes".format(bpop,fpop))

i = 1
while i < 5:
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    print("Year {0}: {1} bunnies and {2} foxes".format(i, bpop_next, fpop_next))
    bpop = bpop_next
    fpop = fpop_next
    i += 1
