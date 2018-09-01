n = 10

def fun1():
    print("n value = ", n)

def fun2():
    global n
    n = n + 2
    print("n value = ", n)

def fun3():
    n = 20
    print("n value = ", n)

fun3()
    
