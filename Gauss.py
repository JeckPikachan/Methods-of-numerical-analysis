import numpy

fname = "matrix.txt"

with open(fname) as f:
    content = f.readlines()

content = [x.strip().split(' ') for x in content]
for i in range(len(content)):
    row = content[i]
    content[i] = list(map(lambda x: float(x), row))

# Getting matrix A
A = [[0] * len(content)] * len(content)
for i in range(len(content)):
    A[i] = content[i][0:-1]


A = numpy.array(A)
if numpy.linalg.det(A) == 0:
    print("det = 0")
    exit()

# Gauss method
for i in range(len(content)):
    currNum = content[i][i]
    for j in range(i + 1, len(content)):
        divNum = content[j][i]
        for k in range(i, len(content[j])):
            content[j][k] = content[j][k] - content[i][k] * (divNum / currNum)

X = [0] * (len(content))
i = 0
for row in reversed(content):
    b = row[len(row) - 1]
    for ind in range(i):
        b -= row[len(row) - 2 - i] * X[len(X) - 1 - i]
    X[len(X) - 1 - i] = b / row[len(row) - 2 - i]
    i += 1

for row in content:
    print(row)

print('\n')
for i in range(len(X)):
    print("X" + str(i + 1) + " = " + str(X[i]))