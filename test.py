k = 10
data = []
for n in range(k):
    p = n + 1
    flag = True
    for j in range(2, p):
        if p % j == 0:
            print(n, j)
            flag = False
            break
    if flag:
        data.append(p)
data.remove(data[0])
print(data)
