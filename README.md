# AI-Powered Media Insights: Dashboard Analisis Strategi Konten

Selamat datang di repositori proyek Mini-Capstone saya. Proyek ini adalah sebuah aplikasi web interaktif yang dibangun untuk menganalisis data performa kampanye media sosial, yang bertujuan untuk mengubah data mentah menjadi *insight* yang dapat ditindaklanjuti bagi para profesional produksi media dan *content strategist*.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dashboard-raihan-saputra.streamlit.app/)

### **[🔗 Kunjungi Live Demo Aplikasi di Sini](https://dashboard-raihan-saputra.streamlit.app/)**

## Tampilan Dashboard
Berikut adalah tampilan dari dashboard interaktif yang telah dibangun:

![Screenshot Dashboard](https://github.com/user-attachments/assets/f99e06e3-71c0-47c7-bece-86d640d8d26f)


## 🌟 Fitur Utama
* **Dashboard Interaktif**: Visualisasi data yang berubah secara dinamis sesuai dengan input pengguna.
* **Filter Data Komprehensif**: Filter data berdasarkan Platform Media Sosial, Influencer, dan Rentang Tanggal.
* **Key Performance Indicators (KPIs)**: Tampilan metrik utama seperti Total Posts, Total Engagements, dan Rata-rata Engagement per Post.
* **Visualisasi Data yang Kaya**:
    * Grafik Batang untuk perbandingan performa antar platform.
    * Diagram Lingkaran (Pie Chart) untuk melihat distribusi sentimen (Positif, Netral, Negatif).
    * Grafik Batang Horizontal untuk merangking top 10 influencer paling berpengaruh.
* **🤖 AI Analyst Assistant**: Didukung oleh Google Gemini, fitur ini memberikan ringkasan analisis dan saran strategis otomatis berdasarkan data yang telah difilter.
* **Tema Kustom**: Tampilan aplikasi yang dipoles dengan tema warna hijau lembut untuk kenyamanan visual.


## 🛠️ Teknologi & Tools yang Digunakan
* **Bahasa**: Python
* **Framework Aplikasi**: Streamlit
* **Analisis Data**: Pandas
* **Visualisasi Data**: Matplotlib & Seaborn
* **Model AI**: Google Gemini
* **Deployment**: Streamlit Community Cloud & GitHub

## 🚀 Cara Menjalankan Proyek Ini Secara Lokal
Jika Anda ingin menjalankan proyek ini di komputer Anda sendiri, ikuti langkah-langkah berikut:

**1. Prasyarat:**
   * Python 3.8+
   * `pip` (Python package installer)

**2. Clone Repository:**
   ```bash
   git clone [https://github.com/r1afif18/Moon1.git](https://github.com/r1afif18/Moon1.git)
   cd Moon1
   ```

**3. Install Dependencies:**
   Install semua library yang dibutuhkan dengan satu perintah:
   ```bash
   pip install -r requirements.txt
   ```

**4. Siapkan API Key:**
   Proyek ini memerlukan API Key dari Google AI.
   * Dapatkan API Key gratis Anda dari [Google AI Studio](https://aistudio.google.com/app/apikey).
   * Saat aplikasi berjalan, masukkan API Key tersebut di kolom yang tersedia pada sidebar.

**5. Jalankan Aplikasi:**
   ```bash
   streamlit run dashboard.py
   ```
   Aplikasi akan terbuka secara otomatis di browser Anda.

## 📂 Struktur File Proyek
```
.
├── streamlit_app.py     # Skrip utama aplikasi Streamlit
├── SwizzleSip.csv       # Dataset yang digunakan
├── requirements.txt     # Daftar library Python yang dibutuhkan
└── README.md            # File yang sedang Anda baca
```

## 🌐 Deployment
Aplikasi ini di-deploy secara online menggunakan **Streamlit Community Cloud**, yang terintegrasi langsung dengan repositori GitHub ini.

---
*Proyek ini dibuat sebagai bagian dari program Mini-Capstone. Dibuat dengan penuh semangat oleh Najmah Fathiinah R.*
