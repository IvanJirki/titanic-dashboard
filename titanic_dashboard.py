import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 💾 Ladataan data
@st.cache_data
def load_data():
    return pd.read_csv("titanic.csv")

df = load_data()

st.title("🚢 Titanic Data Dashboard")

st.subheader("📝 Tietojen yleiskatsaus")
st.dataframe(df.head())

st.subheader("👥 Sukupuolijakauma")
gender_counts = df["Sex"].value_counts()
st.bar_chart(gender_counts)

st.subheader("📊 Ikäjakauma")
fig, ax = plt.subplots()
ax.hist(df["Age"].dropna(), bins=30, edgecolor="black")
ax.set_xlabel("Ikä")
ax.set_ylabel("Matkustajien määrä")
st.pyplot(fig)

st.subheader("🚑 Selviytymisaste")
survival_rate = df["Survived"].value_counts(normalize=True) * 100
st.bar_chart(survival_rate)

st.subheader("🛳 Selviytymisaste matkustusluokittain")
pclass_survival = df.groupby("Pclass")["Survived"].mean() * 100
st.bar_chart(pclass_survival)

st.sidebar.header("⚙ Suodata matkustajia")
age_filter = st.sidebar.slider("Valitse ikä", 0, 80, (0, 80))
filtered_data = df[(df["Age"] >= age_filter[0]) & (df["Age"] <= age_filter[1])]
st.subheader(f"📋 Matkustajat iän välillä {age_filter[0]} - {age_filter[1]}")
st.dataframe(filtered_data)
