# 九九乘法表
for row in range(1, 10):
    for col in range(1, row+1):
        print('{}x{}={}\t'.format(row, col, row*col), end='')
    print()