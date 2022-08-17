import matplotlib.pyplot as plt

#Dados para o gráfico
Dias = ["1","2","3","4","5"]
Valores = [5,7,6,5,8]

#Nome dos eixos
plt.xlabel("Data")
plt.ylabel("valores(R$1 x 1000)")

#Cria o gráfico de colunas
plt.bar(Dias, Valores)

#Mostra o gráfico para o usuário
plt.show()