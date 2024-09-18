F = open('/Users/philipsenn/Desktop/TEST/Test1.txt', 'r')
W = []
for i in F:
  i = i[3::].rstrip().lstrip()
 # i = i[3::]
  if i in W:
     continue
  else:
     W.append(i)
with open('/Users/philipsenn/Desktop/TEST/Test2.txt', 'w') as x:#a will append
  print(sorted(W), file=x)