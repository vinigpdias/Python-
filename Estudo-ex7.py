a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a > b and b > c:
    print(a)

if a > c and c > b:
    print(a)

if b > a and a > c:
    print(b)

if b > c and c > a:
    print(b)

if c > b and b > a:
    print(c)
