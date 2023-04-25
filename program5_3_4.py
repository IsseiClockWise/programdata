sei = []
fu = []
zero = []
for i in range(-10,10):
    if i > 0:
        sei.append(i)
    elif i < 0:
        fu.append(i)
    else:
        zero.append(i)
print(' 正の値 {}'.format(sei))
print(' 負の値 {}'.format(fu))
print(' 零の値 {}'.format(zero))
