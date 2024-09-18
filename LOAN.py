P = int(input('Please input the capital:'))
C = 0
#C = int(input('Please input the charges:'))
M = int(input('Please input the number of months:'))
I = 0.1
A = P / M
c = 0
k = [x for x in range(M)]
for i in k:
    j = (P - A * i) * I
    c = c + j
F = round(A + (C + c) / M)
print(F)
