# for i in range(1, 6):
#     if i <= 3:
#         print("o" * i)
#     else:
#         print("o" * (6-i))

lst = ["o", "o", "o"]

for i in range(1, 5):
    print("".join(lst[:i]))

for i in range(3, 0, -1):
    print("".join(lst[:i]))

