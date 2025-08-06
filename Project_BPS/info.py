import streamlit as st


st.set_page_config(layout="wide")

st.title('Tentang Dashboard Wilkerstat')

st.write("""
    📖 Tutorial Penggunaan Dashboard Monitoring Wilkerstat SE 2026
    ### Fitur dalam Dashboard:
    """)

tab_home, tab_dashboard, tab_chatbot = st.tabs([
    "🏠 Halaman Utama (Home)", 
    "🗺️ Halaman Dashboard Kabupaten/Kota (Lokasi Wilayah)", 
    "💬 Halaman Chatbot"
])


with tab_home:
    st.info("""
        **Setelah membuka dashboard, Anda akan berada di halaman utama Monitoring Wilkerstat Provinsi Jawa Barat**
    """)
    
    st.markdown("##### Halaman ini menyajikan:")

    col1, col2 = st.columns([1, 15])
    with col1:
        st.write("""
        ☞\n
        ☞\n
        ☞\n
        ☞
        """)
    with col2:
        st.write("""
        Jumlah Kabupaten/Kota\n
        Jumlah Kecamatan\n
        Jumlah Desa\n
        Peta interaktif provinsi Jawa Barat lengkap dengan legenda warna berdasarkan kabupaten/kota.
        """)


with tab_dashboard:
    st.write("""
             Setelah memilih salah satu wilayah, Anda akan diarahkan ke halaman dashboard wilayah kabupaten/kota tersebut.

             Langkah-langkah penggunaannya:
             """)
    
    st.markdown("---") 


    st.subheader("1. Pilih Metode Unggah Data :")
    col1, col2 = st.columns(2)
    with col1:
        st.info("☞ **Ganti data sebelumnya:** Menggantikan seluruh data lama dengan data baru.")
    with col2:
        st.success("☞ **Tambahkan ke data sebelumnya:** Menambahkan data baru tanpa menghapus data lama.")
    
    st.subheader("2. Unggah File Data :")
    st.markdown("""
        ☞ Isi label username dan password untuk login.\n
        ☞ Klik tombol "Login".\n
        ☞ Klik tombol "Browse Files".\n
        ☞ Pilih file CSV dari komputer Anda.
    """)
    st.warning("☞ Pastikan file Anda memiliki kolom berikut:")

    st.code("""
id, wid, nama, nm_project, deskripsi_project, iddesa, latitude, longitude, 
accuracy, status, kode_kategori, kategori_landmark, kode_landmark_tipe, 
tipe_landmark, user_created_at, user_upload_at, user_creator_nama, 
photo_url
    """, language="text")

    st.markdown("---") 

    st.subheader("3. Lihat Data yang Telah Diunggah :")
    st.markdown("""
        ☞ Data yang berhasil diunggah akan ditampilkan di tabel "Total Data yang Telah Diunggah".\n
        ☞ Anda dapat memfilter data berdasarkan:
    """)
    st.markdown("""
        ・ Nama Petugas\n
        ・ Kode Wilayah Desa\n
        ・ Nama SLS
    """)
    st.markdown("---")

    st.subheader("4. Visualisasi dan Analisis Data :")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            **☞ Peta Lokasi:** Menampilkan titik landmark berdasarkan data yang diunggah.
            
            **☞ Kartu Ringkasan (Card):**
            
            ・ Jumlah Kecamatan
            
            ・ Jumlah Desa
            
            ・ Jumlah SLS
            
            ・ Total SLS Sukses (≥ 4 landmark)
            
            ・ Total Landmark
        """)
    with col2:
        st.markdown("""
            **☞ Diagram Lingkaran:**
            
            ・ Menampilkan persentase SLS yang sudah sukses dan belum sukses.
            
            **☞ Diagram Batang:**
            
            ・ Menampilkan jumlah landmark yang terlapor per desa dan diurutkan dari yang terbanyak.
        """)

    st.markdown("---")

    st.subheader("5. Tabel Database Kota/Kabupaten :")
    st.markdown("""
        ☞ Tabel ini menampilkan seluruh data terkait wilayah yang Anda pilih.
        
        ☞ Tersedia fitur filter lanjutan berdasarkan:
        
        ・ Kode Wilayah Desa
        
        ・ Nama Kecamatan
        
        ・ Nama Desa
        
        ・ Nama SLS
    """)

with tab_chatbot:
    col1, col2 = st.columns([1, 4], gap="large")

    with col1:

        st.markdown("<br>", unsafe_allow_html=True) 
        st.image("Project_BPS/asset/chatbot.png")

    with col2:
        st.subheader("Langkah-langkah Interaksi")
        st.markdown("""
        1.  Masuk ke menu Chatbot untuk berinteraksi secara langsung dengan sistem.
        2.  Ketikkan pertanyaan Anda di kolom pesan "Tanyakan sesuatu tentang data Wilkerstat".
        3.  Klik tombol Kirim Pesan.
        4.  Sistem akan menjawab pertanyaan Anda berdasarkan data yang tersedia di dashboard.
        """)
        st.info("☞ **Perlu digarisbawahi bahwa chatbot ini di design hanya untuk menjawab pertanyaan seputar database Wilkerstat dan tidak dapat menjawab hal-hal yang bersifat general**")
