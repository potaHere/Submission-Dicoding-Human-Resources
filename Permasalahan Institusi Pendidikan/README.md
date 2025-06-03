# Jaya Jaya Institut - Student Dropout Prediction

## Latar Belakang Proyek
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini menjadi masalah besar untuk institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

## Tujuan Proyek
1. Menganalisis faktor-faktor yang mempengaruhi tingkat dropout mahasiswa
2. Mengembangkan model prediksi untuk mengidentifikasi mahasiswa berisiko dropout
3. Membuat dashboard untuk memantau performa mahasiswa
4. Memberikan rekomendasi untuk mengurangi tingkat dropout

## Struktur Proyek
- `notebook.ipynb`: Berisi analisis data dan pemodelan
- `app.py`: Aplikasi Streamlit untuk prediksi dropout
- `student_dropout_model.pkl`: Model machine learning terlatih
- `preprocessor.pkl`: Pipeline preprocessing data
- `feature_columns.pkl`: Informasi kolom untuk preprocessing
- `requirements.txt`: Daftar package yang diperlukan

## Teknik dan Metode
1. **Data Understanding dan Preprocessing**
   - Analisis data mahasiswa
   - Feature engineering
   - Penanganan outliers dan missing values

2. **Modeling**
   - Implementasi beberapa algoritma machine learning (Random Forest, Gradient Boosting, dll)
   - Hyperparameter tuning
   - Evaluasi model

3. **Deployment**
   - Dashboard interaktif (Metabase)
   - Web app prediktif (Streamlit)

## Dashboard Metabase
Dashboard dibuat menggunakan Metabase untuk memvisualisasikan:
- Distribusi mahasiswa (dropout vs sukses)
- Performa berdasarkan jurusan
- Faktor-faktor utama penyebab dropout
- Tren dropout dari waktu ke waktu

**Akses Dashboard:**
- Email: root@mail.com
- Password: root123

## Aplikasi Prediksi
Aplikasi prediksi berbasis Streamlit memungkinkan staf akademik memasukkan data mahasiswa dan mendapatkan prediksi risiko dropout, beserta rekomendasi tindakan.

**Cara Menjalankan Aplikasi:**
1. Install dependencies: `pip install -r requirements.txt`
2. Jalankan aplikasi: `streamlit run app.py`

## Kesimpulan dan Rekomendasi
Berdasarkan hasil analisis, beberapa rekomendasi action items untuk Jaya Jaya Institut:

1. **Implementasi Sistem Early Warning**:
   - Integrasikan model prediksi dropout ke dalam sistem akademik
   - Set up notifikasi otomatis untuk mahasiswa berisiko tinggi

2. **Program Intervensi Akademik**:
   - Program bimbingan khusus bagi mahasiswa berisiko tinggi
   - Tutor sebaya untuk membantu mahasiswa dengan kesulitan akademik

3. **Dukungan Finansial**:
   - Evaluasi dan perluas program beasiswa berbasis kebutuhan
   - Implementasikan sistem pembayaran yang lebih fleksibel

4. **Peningkatan Keterlibatan Mahasiswa**:
   - Program mentoring antara mahasiswa senior dan junior
   - Tingkatkan kegiatan ekstrakurikuler untuk memperkuat rasa memiliki

5. **Evaluasi Berkelanjutan**:
   - Perbarui model dengan data baru secara berkala
   - Evaluasi efektivitas program intervensi

## Link Streamlit Cloud App
[Student Dropout Prediction App](https://jaya-jaya-institut-dropout-prediction.streamlit.app/)

## Video Demo
[Link to Demo Video](https://youtu.be/demo-video-link)

## Kontak
- Nama: Ja'far Shodiq
- Email: jafarshodiq.alkaf@gmail.com
- ID Dicoding: jafar_shodiq
