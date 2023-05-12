# Calculadora em Python Eduardo 

print("\n*************************** Calculadora em Python ***************************")

print("\nSelecione o número da operação desejada:\n")

print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

x = int(input("\nDigite sua opção (1/2/3/4):"))

if x == 1:
    n1 = float(input("\nDigite o primeiro número:"))
    n2 = float(input("\nDigite o segundo número:"))
    nf = n1 + n2
    print("O resultado da operação",n1, "+",n2, "é =", nf)
elif x == 2:
    n1 = float(input("\nDigite o primeiro número:"))
    n2 = float(input("\nDigite o segundo número:"))
    nf = n1 - n2
    print("O resultado da operação",n1, "-",n2, "é =", nf)
elif x == 3:
    n1 = float(input("\nDigite o primeiro número:"))
    n2 = float(input("\nDigite o segundo número:"))
    nf = n1 * n2
    print("O resultado da operação",n1, "*",n2, "é =", nf)
elif x == 4:
    n1 = float(input("\nDigite o primeiro número:"))
    n2 = float(input("\nDigite o segundo número:"))
    nf = n1 / n2
    print("O resultado da operação",n1, "/",n2, "é =", nf)
else:
    print("Operação invalida")
