import operator

PRECISION = 0.0001


def getNorm(X):
    res = 0
    for x in X:
        res += abs(x)
    return res


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

# Transform to iterations method
for i in range(matrixSize):
    divisor = A[i][i]
    A[i] = [-1 * x / divisor for x in A[i]]
    B[i] /= divisor
    del A[i][i]


# print("A:")
# printMatrix(A)
# print("B:")
# printMatrix(B)

# initial approximation
previousX = [x for x in B]
currentX = [x for x in previousX]
started = False

# iterations
times = 0
while not started or getNorm(list(map(operator.sub, currentX, previousX))) >= PRECISION:
    started = True
    previousX = [x for x in currentX]
    xLen = len(currentX)
    print(str(times) + ": ")
    printX(currentX)
    for i in range(xLen):
        copyX = [x for x in previousX]
        del copyX[i]
        currentX[i] = 0
        for j in range(len(copyX)):
            currentX[i] += copyX[j] * A[i][j]
        currentX[i] += B[i]
    times += 1
    print("Accuracy: " + str(getNorm(list(map(operator.sub, currentX, previousX)))))

print("ITERATIONS:")
printX(currentX)
print("\n==============================================")

# Seidel
previousX = [x for x in B]
currentX = [x for x in previousX]
started = False

times = 0
while not started or getNorm(list(map(operator.sub, currentX, previousX))) >= PRECISION:
    started = True
    previousX = [x for x in currentX]
    xLen = len(currentX)
    print(str(times) + ":")
    printX(currentX)
    for i in range(xLen):
        copyX = [x for x in currentX] # Here is the difference
        del copyX[i]
        currentX[i] = 0
        for j in range(len(copyX)):
            currentX[i] += copyX[j] * A[i][j]
        currentX[i] += B[i]
    times += 1
    print("Accuracy: " + str(getNorm(list(map(operator.sub, currentX, previousX)))))

print("SEIDEL:")
printX(currentX)
