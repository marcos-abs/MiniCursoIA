# Fonte: https://www.perplexity.ai/search/voce-e-um-especialista-em-pyth-4_Tadqk5QdKQVGdyh_v0AQ?0=d#0
import plotly.graph_objects as go

# Data
ids = ["H", "G", "F", "E", "D", "C", "B", "A"]
hrs_sono = [3, 6, 4, 9, 5, 7, 6, 8]
nota = [60, 75, 65, 88, 70, 82, 78, 85]

# Create figure with secondary y-axis
fig = go.Figure()

# Add bar chart
fig.add_trace(go.Bar(
    x=ids,
    y=hrs_sono,
    name='Horas de Sono',
    marker_color='#1FB8CD'
))

# Add line chart
fig.add_trace(go.Scatter(
    x=ids,
    y=nota,
    mode='lines+markers',
    name='Nota',
    line=dict(color='#DB4545', width=3),
    marker=dict(size=8, color='#DB4545')
))

# Update layout
fig.update_layout(
    title='Análise de Dados da Pesquisa Operacional',
    xaxis_title='ID',
    yaxis_title='Valores',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update traces
fig.update_traces(cliponaxis=False)

# Save the chart as both PNG and SVG
fig.write_image("chart.png")
fig.write_image("chart.svg", format="svg")

fig.show()