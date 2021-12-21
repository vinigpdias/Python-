a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a > b and a > c:
    print("Maior: ", a)
    if not (c > a):
        print("Maior: ", c)

if not (b > c):
    print("Maior: ", b)
    if not (c > b):
        print("Maior: ", c)
