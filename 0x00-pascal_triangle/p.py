n = 4
ls = []

for i in range(1, n+1):
    in_ls = []

    for j in range(i):
        if j == 0 or j == i-1:
            n = 1
            in_ls.append(n)
        else:
            in_ls[i-2][j-1] + in_ls[i-2][j]
            in_ls.append(n)
            
    ls.append(in_ls)

for a in ls:
    print(a)

