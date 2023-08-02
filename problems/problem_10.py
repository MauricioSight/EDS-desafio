import streamlit as st
import pandas as pd
import json

# Carrega arquivo
# with open("../data/problem_10_random_dates_0.json", "r") as file:
# with open("../data/problem_10_random_dates_1.json", "r") as file:
with open("../data/problem_10_random_dates_2.json", "r") as file:
    reader = json.load(file)
    df = pd.DataFrame.from_dict({ "Date": reader })

# Redimensionamento por Dia
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)
df["Atendimentos"] = 1
days = df.resample("D").sum()

# Gerar dados
minDate = days.idxmin().dt.strftime('%d/%m/%Y')[0]
maxDate = days.idxmax().dt.strftime('%d/%m/%Y')[0]
minCall = days["Atendimentos"].min()
maxCall = days["Atendimentos"].max()
mean = days["Atendimentos"].mean()

# Escreve na tela
st.write("Quantidade de atendimentos médicos por dia:")
st.line_chart(days)
st.write(f"Mínimo: {minCall}; Máximo: {maxCall}; Média: {round(mean, 2)}")
st.write(f"Intervalo: {minDate} - {maxDate}")
