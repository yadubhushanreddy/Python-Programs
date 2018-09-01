def test(n):
    if n > 1:
        test(n - 1)
    print("AB")
    
test(5)
