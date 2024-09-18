C = int(input('Please input the capital: '))
##i = int(input('Please input the interest in %: ')) / 100
i = 0.1
m = int(input('Please input the number of months: '))
a = C / m
c = 0
k = [x for x in range(m + 1)]
for b in k:
    j = (C - a * b) * i
    c = c + j
d = int(a * 1.01) + c / m
print(d)
