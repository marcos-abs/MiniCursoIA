# Fonte: Gerado pelo DeepSeek (não existe na versão free o compartilhamento da execução)
import json
import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
ids = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
hrs_sono = [8, 6, 7, 5, 9, 4, 6, 3]
notas = [85, 78, 82, 70, 88, 65, 75, 60]

# Criar estrutura JSON ordenada por id em ordem decrescente
dados_pesquisa = {
    "pesquisa_operacional": {
        "titulo": "Análise de Correlação entre Horas de Sono e Notas",
        "amostra": len(ids),
        "variaveis": {
            "independente": "horas_sono",
            "dependente": "nota"
        },
        "participantes": []
    }
}

# Adicionar participantes ordenados por id em ordem decrescente
for i in sorted(range(len(ids)), key=lambda i: ids[i], reverse=True):
    participante = {
        "id": ids[i],
        "dados": {
            "horas_sono": hrs_sono[i],
            "nota": notas[i],
            "categoria_sono": "adequado" if hrs_sono[i] >= 6 else "insuficiente"
        },
        "estatisticas": {
            "desempenho_relativo": round((notas[i] / max(notas)) * 100, 1),
            "eficiencia_sono": round(notas[i] / hrs_sono[i], 1) if hrs_sono[i] > 0 else 0
        }
    }
    dados_pesquisa["pesquisa_operacional"]["participantes"].append(participante)

# Converter para JSON
json_output = json.dumps(dados_pesquisa, indent=2, ensure_ascii=False)
print(json_output)

# Criar visualização
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Notas por Horas de Sono (ordenado decrescente por id)
sorted_indices = sorted(range(len(ids)), key=lambda i: ids[i], reverse=True)
sorted_ids = [ids[i] for i in sorted_indices]
sorted_sono = [hrs_sono[i] for i in sorted_indices]
sorted_notas = [notas[i] for i in sorted_indices]

x_pos = np.arange(len(sorted_ids))
width = 0.35

bars1 = ax1.bar(x_pos - width/2, sorted_sono, width, label='Horas de Sono', alpha=0.8, color='skyblue')
bars2 = ax1.bar(x_pos + width/2, sorted_notas, width, label='Nota (%)', alpha=0.8, color='lightcoral')

ax1.set_xlabel('Participantes (ID)')
ax1.set_ylabel('Valores')
ax1.set_title('Horas de Sono vs Notas por Participante (Ordenado por ID)')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(sorted_ids)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico 2: Correlação entre horas de sono e notas
ax2.scatter(hrs_sono, notas, s=100, alpha=0.7, c='purple', edgecolors='black')
for i, id_val in enumerate(ids):
    ax2.annotate(id_val, (hrs_sono[i], notas[i]), xytext=(5, 5), textcoords='offset points')

# Calcular linha de tendência
z = np.polyfit(hrs_sono, notas, 1)
p = np.poly1d(z)
ax2.plot(hrs_sono, p(hrs_sono), "r--", alpha=0.8, label=f'Tendência: y = {z[0]:.2f}x + {z[1]:.2f}')

ax2.set_xlabel('Horas de Sono')
ax2.set_ylabel('Nota (%)')
ax2.set_title('Correlação entre Horas de Sono e Desempenho')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Estatísticas adicionais
correlacao = np.corrcoef(hrs_sono, notas)[0, 1]
print(f"\nCoeficiente de correlação: {correlacao:.3f}")
print(f"Equação da reta: Nota = {z[0]:.2f} * Sono + {z[1]:.2f}")