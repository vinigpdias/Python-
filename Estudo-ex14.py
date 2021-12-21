numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

teste_1 = numero1 % 2 == 0 and numero2 % 2 == 0
teste_2 = numero1 % 2 == 1 and numero2 % 2 == 1

if teste_1:
    print("Ambos Pares")

if teste_2:
    print("Ambos Impares")
    
else:
    print("Demais Casos")
