a = int
b = int

a = int(input("Digite um número para a: "))
b = int(input("Digite um número para b: "))

#print('{} / {2} = '.format(a))
#print('{} / {2} = '.format(b))

if a % 2 == 0 or b % 2 == 0:
    print("Ao menos um Par")

else:
    print("Nenhum dos dois é par")