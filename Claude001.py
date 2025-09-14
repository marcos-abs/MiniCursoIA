# Fonte: https://claude.ai/share/405d4d61-6311-40dc-81ca-fda8d074a5e8
import json
import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
id_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
hrs_sono = [8, 6, 7, 5, 9, 4, 6, 3]
nota = [85, 78, 82, 70, 88, 65, 75, 60]

# Criando pares de dados e ordenando por ID em ordem decrescente
dados_combinados = list(zip(id_list, hrs_sono, nota))
dados_ordenados = sorted(dados_combinados, key=lambda x: x[0], reverse=True)

# Estruturando JSON com máximo 3 níveis
dados_json = {
    "pesquisa_operacional": {
        "metadata": {
            "total_participantes": len(id_list),
            "variavel_independente": "Horas de Sono",
            "variavel_dependente": "Nota"
        },
        "estatisticas": {
            "sono": {
                "media": round(np.mean(hrs_sono), 2),
                "minimo": min(hrs_sono),
                "maximo": max(hrs_sono)
            },
            "notas": {
                "media": round(np.mean(nota), 2),
                "minimo": min(nota),
                "maximo": max(nota)
            },
            "correlacao": round(np.corrcoef(hrs_sono, nota)[0,1], 3)
        },
        "participantes": [
            {
                "id": participante[0],
                "horas_sono": participante[1],
                "nota": participante[2]
            }
            for participante in dados_ordenados
        ]
    }
}

# Salvando JSON
with open('Claude001.json', 'w', encoding='utf-8') as f:
    json.dump(dados_json, f, indent=2, ensure_ascii=False)

print("JSON gerado:")
print(json.dumps(dados_json, indent=2, ensure_ascii=False))

# Criando visualizações com matplotlib
plt.style.use('default')
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Análise de Dados: Sono vs Desempenho', fontsize=16, fontweight='bold')

# Gráfico 1: Dispersão - Correlação entre Sono e Notas
ax1.scatter(hrs_sono, nota, color='blue', alpha=0.7, s=100)
ax1.set_xlabel('Horas de Sono')
ax1.set_ylabel('Nota')
ax1.set_title('Correlação: Sono vs Nota')
ax1.grid(True, alpha=0.3)

# Linha de tendência
z = np.polyfit(hrs_sono, nota, 1)
p = np.poly1d(z)
ax1.plot(hrs_sono, p(hrs_sono), "r--", alpha=0.8, linewidth=2)

# Gráfico 2: Barras - Horas de Sono por Participante (ordem decrescente por ID)
ids_ordenados = [p[0] for p in dados_ordenados]
sono_ordenado = [p[1] for p in dados_ordenados]
ax2.bar(ids_ordenados, sono_ordenado, color='lightblue', edgecolor='navy')
ax2.set_xlabel('Participante (ID)')
ax2.set_ylabel('Horas de Sono')
ax2.set_title('Horas de Sono por Participante')
ax2.grid(True, alpha=0.3, axis='y')

# Gráfico 3: Barras - Notas por Participante (ordem decrescente por ID)
notas_ordenadas = [p[2] for p in dados_ordenados]
ax3.bar(ids_ordenados, notas_ordenadas, color='lightgreen', edgecolor='darkgreen')
ax3.set_xlabel('Participante (ID)')
ax3.set_ylabel('Nota')
ax3.set_title('Notas por Participante')
ax3.grid(True, alpha=0.3, axis='y')

# Gráfico 4: Histogramas comparativos
ax4.hist(hrs_sono, bins=5, alpha=0.7, label='Horas de Sono', color='skyblue', edgecolor='black')
ax4_twin = ax4.twinx()
ax4_twin.hist(nota, bins=5, alpha=0.7, label='Notas', color='orange', edgecolor='black')
ax4.set_xlabel('Valores')
ax4.set_ylabel('Frequência - Sono', color='blue')
ax4_twin.set_ylabel('Frequência - Notas', color='orange')
ax4.set_title('Distribuição dos Dados')
ax4.legend(loc='upper left')
ax4_twin.legend(loc='upper right')

plt.tight_layout()
plt.show()

# Análise resumida
print("\n=== ANÁLISE RESUMIDA ===")
print(f"Correlação entre sono e notas: {dados_json['pesquisa_operacional']['estatisticas']['correlacao']}")
print(f"Participantes com mais sono tendem a ter notas {'maiores' if dados_json['pesquisa_operacional']['estatisticas']['correlacao'] > 0 else 'menores'}")
print(f"Média de horas de sono: {dados_json['pesquisa_operacional']['estatisticas']['sono']['media']} horas")
print(f"Média das notas: {dados_json['pesquisa_operacional']['estatisticas']['notas']['media']} pontos")