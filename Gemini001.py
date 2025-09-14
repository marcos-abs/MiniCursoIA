import json
import matplotlib.pyplot as plt

# Dados da pesquisa
ids = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
hrs_sono = [8, 6, 7, 5, 9, 4, 6, 3]
notas = [85, 78, 82, 70, 88, 65, 75, 60]

# Criando uma lista de dicionários para cada entrada
dados_pesquisa = []
for i in range(len(ids)):
    dados_pesquisa.append({
        'id': ids[i],
        'horas_sono': hrs_sono[i],
        'nota': notas[i]
    })

# Ordenando os dados decrescentemente por 'id' (assumindo que os IDs são comparáveis como strings ou números)
# Se os IDs fossem numéricos, a ordenação seria direta. Como são letras, a ordem alfabética é utilizada.
# Se uma ordem específica for necessária, um mapeamento seria preciso.
dados_pesquisa_ordenados = sorted(dados_pesquisa, key=lambda x: x['id'])

# Criando a estrutura JSON com no máximo 3 níveis
# O nível 1 é a chave principal 'pesquisa_operacional'.
# O nível 2 é a chave 'resultados', contendo a lista ordenada de dados.
# O nível 3 são os próprios dicionários de dados.
json_output = {
    "pesquisa_operacional": {
        "resultados": dados_pesquisa_ordenados
    }
}

# Convertendo o dicionário Python para uma string JSON formatada
json_string = json.dumps(json_output, indent=4, ensure_ascii=False)

print("--- JSON Gerado ---")
print(json_string)

# --- Visualização com Matplotlib ---

# Preparando os dados para o gráfico
# Vamos plotar as horas de sono e as notas, associadas aos IDs ordenados.
ids_ordenados = [item['id'] for item in dados_pesquisa_ordenados]
horas_sono_ordenadas = [item['horas_sono'] for item in dados_pesquisa_ordenados]
notas_ordenadas = [item['nota'] for item in dados_pesquisa_ordenados]

# Criando o gráfico
fig, ax1 = plt.subplots(figsize=(10, 6))

# Eixo Y para horas de sono
color = 'tab:red'
ax1.set_xlabel('ID do Pesquisado')
ax1.set_ylabel('Horas de Sono', color=color)
ax1.bar(ids_ordenados, horas_sono_ordenadas, color=color, alpha=0.6, label='Horas de Sono')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0, 10) # Limite para horas de sono

# Criando um segundo eixo Y para as notas
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Nota', color=color)
ax2.plot(ids_ordenados, notas_ordenadas, color=color, marker='o', linestyle='-', linewidth=2, label='Nota')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0, 100) # Limite para notas

# Adicionando título e ajustando layout
plt.title('Horas de Sono vs. Nota por ID do Pesquisado')
fig.tight_layout()

# Exibindo a legenda (combinando as de ambos os eixos)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Mostrando o gráfico
plt.show()