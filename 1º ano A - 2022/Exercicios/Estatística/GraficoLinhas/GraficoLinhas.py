import matplotlib.pyplot as plt

#Dados para o gráfico
Dias = ["1","2","3","4","5"]
Valores = [5,7,6,5,8]

#Nome dos eixos
plt.xlabel("Data")
plt.ylabel("valores(R$1 x 1000)")

#determinar os eixos
plt.axis([0,4,0,9])


#=========Cria o gráfico de linhas=========
#o go refere-se às bolinhas verdes
plt.plot(Dias,Valores,"go")

#Altera o tipo e a cor da linha
plt.plot(Dias,Valores,"k:", color="blue")

#==========================================

#Mostra o gráfico para o usuário
plt.show()