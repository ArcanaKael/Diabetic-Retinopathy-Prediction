import streamlit as st
from PIL import Image

def run():
    st.title('Exploration Data Analysis')

    
    st.subheader('Distribusi Data Training')
    image = Image.open('./src/eda1.png')
    st.image(image, caption='figure 1')

    with st.expander('Notes'):
        st.caption('Distribusi pada Data Train adalah 1050 untuk DR (Diabetic Retinopathy) dan 1026 untuk No_DR (No Diabetic Retinopathy).')


    st.subheader('Distribusi Data Validasi')
    image = Image.open('./src/eda2.png')
    st.image(image, caption='figure 2')

    with st.expander('Notes'):
        st.caption('Distribusi pada Data Validation adalah 245 untuk DR (Diabetic Retinopathy) dan 286 untuk No_DR (No Diabetic Retinopathy).')


    st.subheader('Distribusi Ukuran Gambar Data Train')
    image = Image.open('./src/eda3.png')
    st.image(image, caption='figure 3')

    with st.expander('Notes'):
        st.caption('Terlihat bahwa rata-rata tinggi dan lebar gambar untuk masing-masing label DR dan No_DR memiliki nilai yang hampir sama.')


    st.subheader('Distribusi Ukuran Gambar Data Validasi')
    image = Image.open('./src/eda4.png')
    st.image(image, caption='figure 4')

    with st.expander('Notes'):
        st.caption('Terlihat bahwa rata-rata tinggi dan lebar gambar untuk masing-masing label DR dan No_DR memiliki nilai yang hampir sama.')


    st.subheader('Distribusi Intensitas Warna Data Train')
    image = Image.open('./src/eda5.png')
    st.image(image, caption='figure 5')

    with st.expander('Notes'):
        st.caption('Terlihat  bahwa kedua label yaitu DR dan No_DR cenderung memiliki intensitas warna merah (R) yang lebih tinggi.')

    st.subheader('Distribusi Intensitas Warna Data Validasi')
    image = Image.open('./src/eda6.png')
    st.image(image, caption='figure 6')

    with st.expander('Notes'):
        st.caption('Terlihat  bahwa kedua label yaitu DR dan No_DR cenderung memiliki intensitas warna merah (R) yang lebih tinggi.')


    st.subheader('Perbandingan kontur citra retina pada setiap label')
    image = Image.open('./src/eda7.png')
    st.image(image, caption='figure 7')

    with st.expander('Notes'):
        st.caption('Terlihat pada DR terdapat bercak atau bintik-bintik yang mencerminkan adanya lesi, pembuluh darah abnormal atau mikroaneurisma yang merupakan ciri khas dari penyakit DR sedangkan pada label No_DR cenderung menunjukkan kontur pola tepi yang lebih sederhana dan bersih dari bercak-bercak')


    st.subheader('Perbandingan gambar retina pada setiap label')
    image = Image.open('./src/eda8.png')
    st.image(image, caption='figure 8')

    with st.expander('Notes'):
        st.caption('Terlihat  pada gambar DR adanya bercak putih dan kuning, pendarahan kecil serta pola pembuluh darah yang lebih tidak teratur sedangkan gambar No_DR menunjukkan struktur retina yang lebih bersih tanpa adanya kelainan yang mencolok')




