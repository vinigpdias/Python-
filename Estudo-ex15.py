numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    calculo = numero1 - numero2
    print("O primeiro número é maior. Diferença: ", calculo)

if numero2 > numero1:
    calculo = numero2 - numero1
    print("O segundo número é maior. Diferença: ", calculo)
