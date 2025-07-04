# Diabetic Retinopathy Prediction

## 🔗 Project Access

- 📂 **Dataset Source**: [Kaggle – Diagnosis of Diabetic Retinopathy](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy/data)  
- 🚀 **Live App Deployment**: [Hugging Face Space – Diabetic Retinopathy Prediction](https://huggingface.co/spaces/canakael/diabetic-retinopathy-prediction)

---

## 📁 Repository Structure



```
1. README.md                          : Dokumentasi utama proyek
2. project.ipynb                      : Notebook berisi proses EDA hingga model siap deploy
3. model_inference.ipynb              : Notebook inference model
4. deployment folder                  : Folder berisi file deployment untuk menjalankan aplikasi Streamlit di Hugging Face Spaces
```

---

## 🌿 Problem Background

Proyek ini bertujuan untuk mengembangkan sistem otomatis berbasis deep learning yang mampu mendeteksi dan mengklasifikasikan tingkat keparahan **Diabetic Retinopathy** (DR) dari citra retina.

Sistem akan menerima input berupa gambar retina, yang diproses oleh model convolutional neural network untuk memprediksi apakah gambar menunjukkan tanda-tanda DR atau tidak. Model ini dilatih menggunakan dataset yang telah dilabeli ke dalam dua kategori:
- **Diabetic Retinopathy**
- **No Diabetic Retinopathy**

Tujuan dari proyek ini adalah membantu proses diagnosis secara cepat, akurat, dan efisien, khususnya di lingkungan medis dengan keterbatasan tenaga ahli.

---

## 🎯 Project Output

- Model deep learning terbaik dibangun menggunakan **Sequential API**
- Perbandingan performa juga dilakukan dengan **Functional API**
- Notebook untuk deployment inference model
- Aplikasi interaktif berbasis **Streamlit**, di-*deploy* melalui **Hugging Face Spaces**

---

## 🔧 Methodology

Model deep learning dikembangkan menggunakan dua pendekatan utama:

- **Sequential API**: Arsitektur sederhana yang digunakan untuk baseline model CNN  
- **Functional API**: Pendekatan fleksibel untuk menggabungkan layer atau membuat arsitektur model kompleks

📌 Proses yang dilakukan mencakup:
- Preprocessing gambar retina
- Augmentasi data
- Normalisasi pixel
- Evaluasi menggunakan metrik akurasi, loss, dan confusion matrix
- Inference terhadap gambar uji baru

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Matplotlib, Seaborn (visualisasi)
- Streamlit (deployment)
- Hugging Face Spaces (hosting aplikasi)
