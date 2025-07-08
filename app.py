import pandas as pd
import streamlit as st

# Configurações da página
st.set_page_config(page_title="Relatório Contatos Tech", layout="centered")

# Título e descrição
st.title("📊 Relatório de Contatos Tech")
st.markdown(
    """
    Bem-vindo ao painel de consulta dos contatos Tech da Appmax.  
    Cole os User IDs separados por vírgula para filtrar os dados.
    """
)
st.markdown("---")

# Lê os dados da planilha pública no Google Sheets
sheet_id = "1o8WxZootUshy8F7gFMEmmIxDGONtvGvxKjCvBJdgTEI"
aba = "Relat%C3%B3rio%20Contatos%20Tech"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={aba}"

df = pd.read_csv(url)
df.columns = df.columns.str.strip()

# Campo para colar os IDs
ids_input = st.text_area("Cole os User ID Appmax (separados por vírgula):")

if ids_input:
    ids = [i.strip() for i in ids_input.split(",")]
    filtrado = df[df["User ID Appmax"].astype(str).isin(ids)]

    # Define colunas desejadas
    colunas_desejadas = [
        "Nome",
        "E-mail",
        "Número de telefone",
        "Modelo de Negócio",
        "Modelo de negócio qualificação",
        "Status atual RFV",
        "Status Notion"
    ]
    
    resultado = filtrado[colunas_desejadas]

    st.success(f"{resultado.shape[0]} resultados encontrados:")

    # Exibe tabela com largura adaptável
    st.dataframe(resultado, use_container_width=True)

    # Botão para exportar
    csv = resultado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Baixar CSV com resultados",
        data=csv,
        file_name="resultados_filtrados.csv",
        mime="text/csv",
        help="Clique para baixar os resultados filtrados em CSV"
    )
else:
    st.info("Digite ou cole os User IDs acima para iniciar a busca.")

st.markdown("---")
st.caption("Desenvolvido por Heverton Vilas Boas")
