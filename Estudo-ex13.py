a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

if a % 2 == 0 and b % 2 == 0:
    print("Verde")

    if not (a % 2 == 1 and b % 2 == 1):
        print("Vermelho")
    
    else:
        print("Amarelo")

