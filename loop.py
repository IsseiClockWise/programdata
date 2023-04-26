list = ["o", "o", "o"]

for i in range(1, 3):
    print("".join(list[:i]))

for i in range(3, 0, -1):
    print("".join(list[:i]))
