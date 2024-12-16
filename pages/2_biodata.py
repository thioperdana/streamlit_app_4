import streamlit as st

st.title('BIODATA')
st.header("THIO PERDANA")

col_1, col_2 = st.columns([1,2])

with col_1:
    st.image("assets/images/image.jpg", width=40)

    st.subheader("Detail Pribadi")
    st.text("Nama: Thio Perdana")
    st.text("Tanggal Lahir: 23 April 1998")
    st.text("Jenis Kelamin: Laki-Laki")

    st.subheader("Hobby")
    st.text("Olahraga: Sepak Bola")
    st.text("Makanan Favorit: Nasi Goreng")
    st.text("Minuman Favorit: Kopi")

with col_2:
    st.subheader("Alamat")
    st.text("Jalan Raya Bulaksumur No. 123")
    st.text("Kecamatan Bulaksumur")
    st.text("Kabupaten Bekasi")
    st.text("Provinsi Jawa Barat")

    st.subheader("Kegiatan Sehari-Hari")
    st.text("Mengikuti workshop dan kursus online")
    st.text("Mencari informasi lowongan pekerjaan")
    st.text("Merencanakan perjalanan")

    st.subheader("Informasi Kontak")
    st.text("Email: thio.perdana@gmail.com")
    st.text("No. Telpon: 081234567890")
    st.text("Facebook: thioperdana")
    st.text("Instagram: thioperdana")
