

def Fibonacci(n):

    if n <0:
        print("Input is wrong")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(8))

