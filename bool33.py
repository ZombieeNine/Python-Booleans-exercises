def TriangleInequality(A,B,C):
    return (A < B+C) and (B < A+C) and (C < A+B)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
X=(TriangleInequality(a,b,c))
print("Существует треугольник со сторонами a, b, c? ", X)
