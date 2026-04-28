n = int(input("Qual número você quer a tabuada até 25: "))
for c in range(26):
    print(f"{n}.{c:2} = {n*c}")