def TriangleInequality(A,B,C):
    return (A < B+C) and (B < A+C) and (C < A+B)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
X=(a==b and a==c)
print("Треугольник является равносторонним? ", X)