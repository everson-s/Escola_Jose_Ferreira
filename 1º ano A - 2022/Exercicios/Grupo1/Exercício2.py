#Determinar o IMC de uma pessoa

M = float(input("Digite a sua massa: "))
A = float(input("Digite a sua altura: "))

IMC = M / (A**2)

print("O seu IMC é igual a {}".format(IMC))