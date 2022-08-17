import matplotlib.pyplot as plt

#Dados para o gráfico
Dias = ["1","2","3","4","5"]
Valores = [5,7,6,5,8]

#Nome dos eixos
plt.xlabel("valores(R$1 x 1000)")
plt.ylabel("Data")

#Cria o gráfico de colunas
plt.barh(Dias, Valores)

#Mostra o gráfico para o usuário
plt.show()