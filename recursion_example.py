def test(n):
    print("A")
    if n > 1:
        test(n - 1)
    print("B")
    
test(5)
