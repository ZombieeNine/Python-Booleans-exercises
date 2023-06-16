
A=float(input("A: "))
B=float(input("B: "))
C=float(input("C: "))
print("A={0}, B={1}, C={2}".format(A,B,C))
D=B*B-4*A*C
x=(D>=0)
print("Дискриминант", D)
print("Квадр. уравнение {0}x^2+{1}x+{2}=0 имеет вещественные корни?".format(A,B,C), x)
