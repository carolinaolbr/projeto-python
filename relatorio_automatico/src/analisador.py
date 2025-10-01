import pandas as pd
import matplotlib.pyplot as plt

def ler_dados(caminho):
    df = pd.read_csv(caminho)
    df['Total'] = df['Quantidade'] * df['Valor_Unitario']
    return df

def gerar_resumo(df):
    total_vendas = df['Total'].sum()
    media_vendas = df['Total'].mean()
    vendas_por_vendedor = df.groupby('Vendedor')['Total'].sum().to_dict()

    resumo = {
        'total_vendas': total_vendas,
        'media_vendas': media_vendas,
        'vendas_por_vendedor': vendas_por_vendedor,
    }
    return resumo

def gerar_grafico(vendas_por_vendedor, caminho_imagem):
    vendedores = list(vendas_por_vendedor.keys())
    valores = list(vendas_por_vendedor.values())

    plt.figure(figsize=(8, 6))
    plt.bar(vendedores, valores, color='skyblue')
    plt.title('Vendas por Vendedor')
    plt.xlabel('Vendedor')
    plt.ylabel('Total Vendido (R$)')
    plt.tight_layout()
    plt.savefig(caminho_imagem)
    plt.close()
