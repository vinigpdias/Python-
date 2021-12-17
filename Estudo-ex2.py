delta = int
#a, b, c = int

#variáveis
#x1, x2, delta, raiz = int

#início
x1 = 0
x2 = 0
#delta = 0
raiz = 0
a = int(input("Digite valor de a "))
b = int(input("Digite valor de b "))
c = int(input("Digite valor de c "))


if a == 0:
    print("Não existe raiz")
   
delta = b*b -4*a*c

if delta < 0:
    print("A equação não tem raízes reais")

else:
    print("A equação tem raízes reais")
    