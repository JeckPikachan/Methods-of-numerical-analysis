import numpy
import math


def finMaxInMatrix(A):
    imax = 0
    jmax = 1
    maxEl = abs(A[0][1])
    length = len(A)
    for i in range(length):
        for j in range(i + 1, length):
            if abs(A[i][j]) > maxEl:
                maxEl = abs(A[i][j])
                imax = i
                jmax = j

    return {'i': imax, 'j': jmax}


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


def oneOrZero(x, y):
    if x == y:
        return 1
    return 0


# printMatrix(numpy.linalg.eig(A)[1])

U = UT = T = [[oneOrZero(x, y) for y in range(matrixSize)] for x in range(matrixSize)]

for i in range(100):
    res = finMaxInMatrix(A)
    fi = math.atan(2 * A[res['i']][res['j']] / (A[res['i']][res['i']] - A[res['j']][res['j']])) / 2
    U = [[oneOrZero(x, y) for y in range(matrixSize)] for x in range(matrixSize)]
    U[res['i']][res['i']] = U[res['j']][res['j']] = math.cos(fi)
    U[res['j']][res['i']] = math.sin(fi)
    U[res['i']][res['j']] = -math.sin(fi)
    UT = numpy.transpose(U)
    T = numpy.matmul(T, U)
    A = numpy.matmul(numpy.matmul(UT, A), U)


X = [0] * matrixSize
for i in range(matrixSize):
    X[i] = A[i][i]

printX(X)

printMatrix(T)