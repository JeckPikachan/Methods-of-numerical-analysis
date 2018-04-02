import numpy
import math


def printX(X):
    lenX = len(X)
    for i in range(lenX):
        print("X" + str(i + 1) + " = " + str(X[i]))


def printMatrix(A):
    for row in A:
        print(row)


fname = "matrix.txt"

with open(fname) as f:
    content = f.readlines()

content = [x.strip().split(' ') for x in content]
matrixSize = len(content)
for i in range(matrixSize):
    row = content[i]
    content[i] = list(map(lambda x: float(x), row))

# Getting matrix A
A = [[0] * matrixSize] * matrixSize
for i in range(matrixSize):
    A[i] = content[i][0:-1]

# Getting vector B
B = [0] * matrixSize
for i in range(matrixSize):
    B[i] = content[i][-1]

AT = numpy.transpose(A)

A = numpy.matmul(AT, A)
B = numpy.matmul(AT, B)

U = [[0] * matrixSize for x in range(matrixSize)]

for i in range(matrixSize):
    for j in range(i, matrixSize):
        sum = A[i][j]
        for k in range(i):
            sum -= U[k][i] * U[k][j]
        if i == j:
            U[i][j] = math.sqrt(sum)
        else:
            U[i][j] = sum / U[i][i]

UT = numpy.transpose(U)
Y = numpy.linalg.solve(UT, B)
X = numpy.linalg.solve(U, Y)

printX(X)

detA = 1
for i in range(matrixSize):
    detA *= U[i][i] ** 2

print("\nDET(A): " + str(detA))

AInv = [[0]*matrixSize for x in range(matrixSize)]

for i in range(matrixSize):
    e = [0] * matrixSize
    e[i] = 1
    Y = numpy.linalg.solve(UT, e)
    AInv[i] = numpy.linalg.solve(U, Y)

AInv = numpy.transpose(AInv)
print("\nInverted Matrix:")
printMatrix(AInv)


print("det(A): " + str(detA))