a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a > b:
    d = a
    a = b
    b = d

if a > c:
    d = a
    a = c
    c = d

if b > c:
    d = b
    b = c
    c = d

print(a, " ", b, " ", c)