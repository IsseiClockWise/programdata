def two_dimension_array(line = 2, col = 2):
    x = []
    for i in range(line):
        y = []
        for j in range(col):
            y.append(i+j)
        x.append(y)
    for i in range(line):
        print(x[i])
    return x
arrays = two_dimension_array(4)
print(arrays[1][1])
