import matplotlib.pyplot as plt


Meses = ["Janeiro", "Fevereiro","Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
Salario = [2000,2300,2500,2600,3000,3200,1500,2000,6000,1300,1800,5000]

plt.ylabel("Salário (R$)")
plt.xlabel("Meses")
plt.title("Salário mensal - 2022")
#plt.grid(True)
plt.bar(Meses, Salario,color=(.45,.48,.48))

#Inclinar os labels do eixo x em 45°:
plt.xticks(rotation=45)

plt.show()