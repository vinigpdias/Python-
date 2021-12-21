numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
calculo = ["somar", "subtrair", "multiplicar", "dividir", "diferença"]
opção = str(input("+, -, *, /, %.\nSelecione o tipo de cálculo que deseja :"))


#if opção +:

if opção == "+":
    calculo = numero1 + numero2
    print("O resultado da soma é: ", calculo)

if opção == "-":
    calculo = numero1 - numero2
    print("O resultado da subtração é: ", calculo)

if opção == "*":
    calculo = numero1 * numero2
    print("O resultado da multiplicação é: ", calculo)

if opção == "/":
    calculo = numero1 / numero2
    print("O resultado da divisão é: ", calculo)

if opção == "%":
    calculo = numero1 % numero2
    print("O resultado da diferença é: ", calculo)