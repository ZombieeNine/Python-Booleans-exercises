def TriangleInequality(A,B,C):
    return (A < B+C) and (B < A+C) and (C < A+B)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
X=(a*a==b*b+c*c)\
    or (b*b==a*a+c*c)\
        or (c*c==a*a+b*b)
print("Треугольник является прямоуголным? ", X)
# рабочий пример стороны треугольника со значениями 3,4,5.