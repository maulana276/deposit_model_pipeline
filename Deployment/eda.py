import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def run():
    st.title('Welcome to my WebApps!')
    st.write('halo')

    df = pd.read_csv('Predict-term-deposit.csv')
    st.table(df.head(5))


    deposit_pie = df.groupby('y')['Id'].mean()
    # Data untuk pie chart
    labels = deposit_pie.index
    sizes = deposit_pie.values

    # Menampilkan judul di aplikasi Streamlit
    st.title('Persentase Deposito Nasabah')

    # Menggunakan plotly untuk membuat pie chart di Streamlit
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title('Persentase Deposito Nasabah')
    ax.axis('equal')  # Memastikan pie chart berbentuk lingkaran

    # Menampilkan pie chart di aplikasi Streamlit
    st.pyplot(fig)
    st.text('Pada data ini persentase nasabah yang berlangganan deposito 60.7%, sedangkan nasabah yang tidak berlangganan adalah 39.3%')

    st.subheader("Bar Plot Education-Balance")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Tampilkan scatter plot campaign-month
    st.subheader("Scatter Plot Campaign-Month")
    scatter_fig, scatter_ax = plt.subplots()
    sns.scatterplot(data=df, y="campaign", x="month", hue="y", palette="bright", ax=scatter_ax)
    scatter_ax.set_xlabel('Month')
    scatter_ax.set_ylabel('Campaign')
    st.pyplot(scatter_fig)
    st.text('Nasabah yang dihubungi lebih sedikit dalam promosi produk deposito lebih banyak yang berlangganan dibanding nasabah yang dihubungi lebih sering')

    # Tampilkan barplot status-age
    st.subheader("Bar Plot Status-Age")
    barplot_fig, barplot_ax = plt.subplots()
    sns.barplot(data=df, x="marital", y="age", hue="y", palette="bright", ax=barplot_ax)
    barplot_ax.set_xlabel('Marital')
    barplot_ax.set_ylabel('Age')
    st.pyplot(barplot_fig)
    st.text('- Rata-rata umur nasabah memiliki rentang anatara 30 sampai 50 tahun')
    st.text('- Nasabah dengan status cerai lebih banyak yang sudah berlangganan deposito, sedangkan nasabah dengan status single lebih banyak yang tidak berlangganan deposito')

    # Barplot education-balance tanpa hue y
    average_purchases = df.groupby('education')['balance'].mean()
    ax1.bar(average_purchases.index, average_purchases.values, alpha=0.5)
    ax1.set_xlabel('Education')
    ax1.set_ylabel('Balance')
    ax1.set_title('Education on Balance')

    # Barplot education-balance dengan hue y
    sns.barplot(data=df, x="education", y="balance", hue="y", palette="bright", ax=ax2)
    ax2.set_xlabel('Education')
    ax2.set_ylabel('Balance')
    ax2.set_title('Education on Balance with y Hue')
    st.pyplot(fig)
    st.text('- Nasabah  dengan latar pendidkan perguruan tinggi memiliki lebih banyak saldo di dalam akunnya, sedangkan dengan latar belakang sekolah menengah  memiliki saldo paling sedikit')
    st.text('- Nasabah yang berlangganan produk deposito paling banyak terdapat pada nasabah dengan latar pendidikan yang tidak disebutkan dan dengan latar perguruan tinggi')


    # Tampilkan barplot last campaign outcome dengan hue y
    st.subheader("Bar Plot Last Campaign Outcome")
    poutcome_fig, poutcome_ax = plt.subplots()
    sns.barplot(data=df, x="poutcome", y="Id", hue="y", palette="bright", ax=poutcome_ax)
    poutcome_ax.set_title('Hasil Campaign Sebelumnya')
    st.pyplot(poutcome_fig)
    st.text('- Nasabah yang gagal berlangganan pada campaign sebelumnya, berhasil berlangganan pada campaign sekarang.')
    st.text('- Nasabah yang bukan target pada campaign sebelumnya, berhasil berlangganan pada campaign sekarang.')

