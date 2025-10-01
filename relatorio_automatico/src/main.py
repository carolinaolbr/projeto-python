import os
from analisador import ler_dados, gerar_resumo, gerar_grafico
from gerador_relatorio import gerar_pdf

def main():
    # Caminho base do projeto
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Caminhos absolutos
    caminho_csv = os.path.join(BASE_DIR, "dados", "vendas.csv")
    caminho_grafico = os.path.join(BASE_DIR, "relatorios", "grafico_vendas.png")
    caminho_pdf = os.path.join(BASE_DIR, "relatorios", "relatorio_vendas.pdf")

    # Executar etapas
    df = ler_dados(caminho_csv)
    resumo = gerar_resumo(df)
    gerar_grafico(resumo['vendas_por_vendedor'], caminho_grafico)
    gerar_pdf(resumo, caminho_pdf, caminho_grafico)

    print("Relatório com gráfico gerado com sucesso!")

if __name__ == "__main__":
    main()
    

