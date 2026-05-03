import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. LEITURA DOS DADOS
# =========================
df = pd.read_excel("Análise de Eficiência Produtiva.xlsx")

# =========================
# 2. TRATAMENTO
# =========================
df["Taxa_Defeito"] = df["Quantidade_Defeituosa"] / df["Quantidade_Produzida"]

# =========================
# 3. ANÁLISES
# =========================

# Por máquina
media_maquina = df.groupby("Maquina")["Taxa_Defeito"].mean()
print("\nDefeito por máquina:")
print(media_maquina)

# Por turno
media_turno = df.groupby("Turno")["Taxa_Defeito"].mean()
print("\nDefeito por turno:")
print(media_turno)

# Por operador
media_operador = df.groupby("Operador")["Taxa_Defeito"].mean()
print("\nDefeito por operador:")
print(media_operador)

# Cruzamento operador + máquina
tabela_op_maquina = df.groupby(["Operador", "Maquina"])["Taxa_Defeito"].mean()
print("\nOperador x Máquina:")
print(tabela_op_maquina)

# =========================
# 4. VISUALIZAÇÃO
# =========================

media_maquina.plot(kind="bar")

plt.title("Taxa de Defeito por Máquina")
plt.ylabel("Taxa de Defeito")
plt.xlabel("Máquina")

plt.show()

#GRÁFICO 1  Defeito por Operadorins

media_turno = df.groupby("Turno")["Taxa_Defeito"].mean()

media_turno.plot(kind="bar")

plt.title("Taxa de Defeito por Turno")
plt.ylabel("Taxa de Defeito")
plt.xlabel("Turno")

plt.show()


# PARETO - TIPOS DE DEFEITO
# =========================

# Contagem
pareto = df["Tipo_Defeito"].value_counts()

# DataFrame
pareto_df = pareto.reset_index()
pareto_df.columns = ["Tipo_Defeito", "Quantidade"]

# % acumulado
pareto_df["Percentual_Acumulado"] = pareto_df["Quantidade"].cumsum() / pareto_df["Quantidade"].sum()

# Gráfico
fig, ax1 = plt.subplots()

ax1.bar(pareto_df["Tipo_Defeito"], pareto_df["Quantidade"])
ax1.set_xlabel("Tipo de Defeito")
ax1.set_ylabel("Quantidade")

ax2 = ax1.twinx()
ax2.plot(pareto_df["Tipo_Defeito"], pareto_df["Percentual_Acumulado"], marker="o")
ax2.set_ylabel("Percentual Acumulado")

plt.title("Gráfico de Pareto - Tipos de Defeito")

plt.show()

