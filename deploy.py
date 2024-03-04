import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.header("Bike Sharing")


#import data
df = pd.read_csv("Dashboard\clean_df.csv")


with st.sidebar:
    markdown = """
    - **Nama:** Delvin Nuryadi
    - **ID Dicoding:** delvinnuryadi
    """
    st.markdown(markdown)


# visualisasi sepanjang 2012
with st.container():
    
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["year"].astype(str)
    year_2012_df = df[df["year"] == "2012"]
    monthly_casual_2012_df = year_2012_df.resample(rule='M', on="date").agg({
    'casual' : 'sum'
    })
    monthly_casual_2012_df.index = monthly_casual_2012_df.index.strftime('%B')


    fig, ax = plt.subplots()
    ax.plot(monthly_casual_2012_df.index, monthly_casual_2012_df["casual"],
            marker='o',
            color='red')
    ax.set_xlabel('Bulan (2012)')
    ax.set_ylabel('Jumlah casual users')
    ax.set_title('Trend casual users 2012')
    ax.set_xticklabels(monthly_casual_2012_df.index,rotation=45)
    ax.grid(True)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    #visualisasi jumlah casual user disetiap musim dari 2011 sampai 2012
    with st.container():
        colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
        # st.write("Casual user by season 2011-2012")
        byseason_users_df = df.groupby("season")["casual"].sum().reset_index()
        byseason_users_df = byseason_users_df.sort_values("casual", ascending=False)
        fig, ax = plt.subplots(figsize=(20,23))
        ax.bar(byseason_users_df["season"], 
            byseason_users_df["casual"],
            color = colors)
        ax.set_title('Jumlah casual user tiap musim 2011-2012', fontsize=50)
        ax.tick_params(axis='y', labelsize=50)
        ax.tick_params(axis='x', labelsize=45)
        st.pyplot(fig)




with col2:
    # Visualisasi persentase perbandingan jumlah casual user tahun 2011 dan 2012
    with st.container():
        byyear_casual_df = df.groupby("year")["casual"].sum().reset_index()
        labels = ["2011", "2012"]
        fig, ax = plt.subplots()
        ax.set_title('perbandingan casual users 2011 vs 2012')
        ax.pie(byyear_casual_df["casual"],
            labels = labels,
            autopct = '%1.0f%%',)
        
        st.pyplot(fig)




