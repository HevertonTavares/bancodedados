import pandas as pd
import streamlit as st
import re

st.title("📊 Relatório de Contatos Tech")

sheet_id = "1o8WxZootUshy8F7gFMEmmIxDGONtvGvxKjCvBJdgTEI"
aba = "Relat%C3%B3rio%20Contatos%20Tech"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={aba}"

df = pd.read_csv(url)
df.columns = df.columns.str.strip()

ids_input = st.text_area("Cole os User ID Appmax (separados por vírgula, espaço ou enter):")

if st.button("🔍 Pesquisar"):
    if ids_input.strip() == "":
        st.warning("Por favor, cole os IDs para pesquisar.")
    else:
        ids = re.split(r"[,\s]+", ids_input.strip())
        filtrado = df[df["User ID Appmax"].astype(str).isin(ids)]

        colunas_desejadas = [
            "Nome",
            "E-mail",
            "Número de telefone",
            "Modelo de Negócio",
            "Modelo de negócio qualificação",
            "Status atual RFV",
            "Status Notion"
        ]

        # Inclui a coluna ID antes das colunas desejadas
        resultado = filtrado[["User ID Appmax"] + colunas_desejadas]

        st.success(f"{resultado.shape[0]} resultados encontrados:")
        st.dataframe(resultado, use_container_width=True)

        csv = resultado.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Baixar CSV com resultados",
            data=csv,
            file_name="resultados_filtrados.csv",
            mime="text/csv"
        )
else:
    st.info("Digite ou cole os User IDs acima e clique em Pesquisar para iniciar a busca.")

st.markdown("---")
st.caption("Desenvolvido por Heverton Vilas Boas")
