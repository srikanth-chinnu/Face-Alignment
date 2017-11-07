with open('outputValues/results.txt') as f:
    lines = f.readlines()
a = []
for i in range(len(lines)):
    count1 = 0
    count2 = 0
    b = ""
    for j in range(len(lines[i])):
        if(count1==2 and lines[i][j]!='.'):
            b = b + (lines[i][j])
        if(lines[i][j]=='.'):
            count1 += 1
        if(lines[i][j]==' '):
            count2 = 1
        if(count2==1):
            b = b + (lines[i][j])
    a.append(b)

a.sort()
for i in range(len(a)):
    print(a[i]),
