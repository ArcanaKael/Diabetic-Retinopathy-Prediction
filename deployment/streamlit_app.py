import streamlit as st
import eda
import prediction

# Konfigurasi halaman (harus paling atas)
st.set_page_config(page_title="Diabetic Retinopathy App", layout="centered")

# Routing halaman
PAGES = {
    "Exploration Data Analysis": eda,
    "Prediction": prediction
}

# Pilih halaman di sidebar
page = st.sidebar.selectbox(label='📌 Select Page:', options=['Introduction', 'Exploration Data Analysis', 'Prediction'])

# ---------------- INTRODUCTION ----------------
if page == 'Introduction':
    st.title("👁️ Diabetic Retinopathy Prediction")

    # Tampilkan gambar besar tanpa kolom
    st.image('./src/image.jpeg', caption='Illustration of Retinal Image')

    st.markdown("---")

    # Toggle antara objective dan kesimpulan
    selection = st.radio("📌 Pilih informasi yang ingin ditampilkan:", 
                         options=["Project Objective", "Kesimpulan Proyek"], 
                         horizontal=True)

    if selection == "Project Objective":
        st.markdown("""
        ## 🎯 Project Objective  
        Memprediksi **Diabetic Retinopathy (DR)** dari citra retina menggunakan pendekatan **Computer Vision** berbasis Deep Learning.  
        Tujuannya adalah membantu deteksi dini untuk mengurangi risiko komplikasi berat, seperti kebutaan.
        """)

    elif selection == "Kesimpulan Proyek":
        st.markdown("""
        ## 📋 Kesimpulan Proyek

        **Dataset & Preprocessing:**  
        Dataset berasal dari Kaggle dan terbagi menjadi train, validation, dan test set dengan distribusi kelas seimbang.  
        Setelah augmentasi, jumlah data meningkat signifikan terutama pada train set, membantu memperkaya variasi data dan mengurangi overfitting.

        **Modeling & Evaluasi:**  
        Dua model diuji: Sequential dan Functional. Model Sequential menunjukkan performa terbaik karena lebih stabil, presisi tinggi, dan andal dalam mendeteksi DR.

        **Insight Bisnis:**  
        Model berpotensi tinggi diimplementasikan dalam sistem klinis sebagai alat bantu diagnosis otomatis.  
        Ini dapat mempercepat skrining, mengurangi beban dokter, dan memperluas layanan di wilayah minim fasilitas.

        **Rekomendasi Implementasi:**  
        Uji di data dunia nyata, integrasikan ke sistem EMR, dan lakukan pembaruan berkala untuk menjaga akurasi dan relevansi.
        """)

    st.markdown("➡️ Silakan pilih menu lainnya melalui sidebar di kiri untuk menjelajahi EDA dan melakukan prediksi.")

# ---------------- EDA PAGE ----------------
elif page == 'Exploration Data Analysis':
    eda.run()

# ---------------- PREDICTION PAGE ----------------
else:
    prediction.run()