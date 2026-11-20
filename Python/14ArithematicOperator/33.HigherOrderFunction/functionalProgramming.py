def Operate(num,operation):
    return operation(num)


def cube(n):
    return n*n*n

print(Operate(5,cube))

