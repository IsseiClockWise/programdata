lst = ["o", "o", "o"]

for i in range(1, 3):
    print("".join(lst[:i]))

for i in range(3, 0, -1):
    print("".join(lst[:i]))
