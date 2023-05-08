def fibSeq(n):
    a, b, c= 1, 1, 1
    while c <= n:
        print("Fibonacci number",c,"is", a, end=".\n")
        a, b = b, a+b
        c += 1


fibSeq(int(input("Enter Fibonacci number to count to: ")))
