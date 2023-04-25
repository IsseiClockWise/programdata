kisu = []
gusu = []
for i in range(1,11):
    gusu.append(i) if i % 2 == 0 else kisu.append(i)
print(' 奇数：{}'.format(kisu))
print(' 偶数：{}'.format(gusu))
