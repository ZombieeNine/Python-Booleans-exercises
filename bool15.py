a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
d=(a>0)
e=(b>0)
f=(c>0)
g=(d and e and not f) \
    or (d and f and not e)\
        or(f and e and not d)
print(g)