file = open("stuff.txt", "w")

for i in range (10001):
    file.write(f"\n    elif number == {i} and number >= range1 and number <= range2:\n        print('{i}')\n        a=2\n")
