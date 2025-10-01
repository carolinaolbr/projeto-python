from fpdf import FPDF

def gerar_pdf(resumo, caminho_pdf, caminho_imagem):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Relatório de Vendas", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Total de Vendas: R$ {resumo['total_vendas']:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Média de Vendas: R$ {resumo['media_vendas']:.2f}", ln=True)
    pdf.ln(10)

    pdf.cell(200, 10, txt="Vendas por Vendedor:", ln=True)
    for vendedor, total in resumo['vendas_por_vendedor'].items():
        pdf.cell(200, 10, txt=f"{vendedor}: R$ {total:.2f}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt="Gráfico de Vendas por Vendedor:", ln=True)
    pdf.image(caminho_imagem, x=30, y=pdf.get_y(), w=150)

    pdf.output(caminho_pdf)
