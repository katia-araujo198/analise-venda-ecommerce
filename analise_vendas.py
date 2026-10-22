import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulando um Dataset de E-commerce
np.random.seed(42)
n_linhas = 100
categorias = ['Eletrônicos', 'Vestuário', 'Casa', 'Beleza']

dados = {
    'ID_Transacao': range(1, n_linhas + 1),
    'Categoria': np.random.choice(categorias, n_linhas),
    'Preco_Unitario': np.random.uniform(50.0, 1000.0, n_linhas).round(2),
    'Quantidade': np.random.randint(1, 4, n_linhas)
}

df = pd.DataFrame(dados)
df['Faturamento_Total'] = df['Preco_Unitario'] * df['Quantidade']

print("--- Resumo dos Dados ---")
print(df.head())
print("\nFaturamento Total por Categoria:")
print(df.groupby('Categoria')['Faturamento_Total'].sum())
