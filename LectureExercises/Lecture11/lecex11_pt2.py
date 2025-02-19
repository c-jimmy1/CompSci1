hd = input("Enter Dale's height: ").strip()
print(hd)
hd = int(hd)

he = input("Enter Erin's height: ").strip()
print(he)
he = int(he)

hs = input("Enter Sam's height: ").strip()
print(hs)
hs = int(hs)

if hd > he:
    if hd > hs:
        print("Dale")
        if he > hs:
            print("Erin")
            print("Sam")
        else:
            print("Sam")
            print("Erin")
    else:
        print("Sam")
        print("Dale")
        print("Erin")
else:
    if he > hs:
        print("Erin")
        if hd > hs:
            print("Dale")
            print("Sam")
        else:
            print("Sam")
            print("Dale")
    else:
        print("Sam")
        print("Erin")
        print("Dale")