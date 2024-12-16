import streamlit as st

st.title('BIODATA')
st.header("THIO PERDANA")

col_1, col_2 = st.columns([1,2])

with col_1:
    st.subheader("Detail Pribadi")
    st.text("Nama: Thio Perdana")
    st.text("Tanggal Lahir: 23 April 1998")
    st.text("Jenis Kelamin: Laki-Laki")

with col_2:
    st.subheader("Alamat")
    st.text("Jalan Raya Bulaksumur No. 123")
    st.text("Kecamatan Bulaksumur")
    st.text("Kabupaten Bekasi")
    st.text("Provinsi Jawa Barat")
