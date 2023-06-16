def TriangleInequality(A,B,C):
    return (A < B+C) and (B < A+C) and (C < A+B)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
X=(a==b or a==c or b==c)
print("Треугольник является равнобедренным? ", X)