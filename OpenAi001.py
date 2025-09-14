# Fonte: https://chatgpt.com/share/68c7234c-51f0-8008-8b70-5d6230ab6735
import matplotlib.pyplot as plt

# Dados
id = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
hrs_sono = [8, 6, 7, 5, 9, 4, 6, 3]
nota = [85, 78, 82, 70, 88, 65, 75, 60]

# Ordenar por id em ordem decrescente
dados = list(zip(id, hrs_sono, nota))
dados.sort(key=lambda x: x[0], reverse=True)

ids_ord, hrs_ord, notas_ord = zip(*dados)

# Gráfico
plt.figure(figsize=(8,5))
plt.scatter(hrs_ord, notas_ord, color='blue', s=100)

for i, txt in enumerate(ids_ord):
    plt.annotate(txt, (hrs_ord[i]+0.1, notas_ord[i]-1))

plt.title("Relação entre Horas de Sono e Nota")
plt.xlabel("Horas de Sono")
plt.ylabel("Nota")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
