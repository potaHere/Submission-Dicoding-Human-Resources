# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding
Jaya Jaya Maju adalah perusahaan multinasional yang didirikan sejak tahun 2000, dengan lebih dari 1.000 karyawan tersebar di seluruh negeri. Meskipun telah berkembang pesat, perusahaan ini menghadapi tantangan signifikan dalam pengelolaan sumber daya manusia. Salah satu masalah utama yang dihadapi adalah tingginya tingkat keluarnya karyawan (attrition rate) yang mencapai 16,92% - jauh di atas rata-rata industri yang ideal. Tingginya angka ini menunjukkan adanya permasalahan dalam mempertahankan karyawan, yang berdampak negatif pada produktivitas, biaya rekrutmen, dan stabilitas operasional.


### Permasalahan Bisnis

Berikut adalah masalah utama yang dihadapi oleh perusahaan Jaya Jaya Maju:

1. **Tingginya tingkat attrition rate** yang mencapai 16,92%, jauh di atas rata-rata industri yang sehat (10-12%)
2. **Ketidakseimbangan beban kerja** yang mengakibatkan banyak karyawan harus melakukan lembur
3. **Ketidakpuasan karyawan muda** terutama pada kelompok usia di bawah 35 tahun
4. **Tingginya turnover di departemen Sales dan R&D** yang berdampak pada produktivitas departemen tersebut
5. **Struktur kompensasi** yang kurang kompetitif untuk level karyawan tertentu
6. **Sistem pengembangan karir** yang belum jelas terutama pada tahun-tahun kritis (1 tahun, 2-3 tahun, dan 6-7 tahun masa kerja)


### Cakupan Proyek

- **Analisis Data**: Menggunakan data karyawan untuk mengidentifikasi faktor-faktor utama yang mempengaruhi attrition
- **Visualisasi & Dashboard**: Mengembangkan dashboard interaktif untuk membantu tim HR memantau dan menganalisis tren attrition
- **Pemodelan Prediktif**: Membuat model machine learning untuk memprediksi karyawan yang berisiko tinggi keluar
- **Rekomendasi Strategis**: Memberikan saran praktis berdasarkan temuan analisis untuk mengurangi tingkat attrition


### Persiapan

#### Sumber Data
Dataset yang digunakan adalah data karyawan Jaya Jaya Maju yang dapat diakses melalui [repositori Dicoding](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).

#### Setup Environment - Anaconda
```bash
conda create --name hr-analytics python=3.9
conda activate hr-analytics
pip install -r [requirements.txt](http://_vscodecontentref_/1)
```

#### Setup Environment - Shell/Terminal

```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

#### Setup Metabase
```bash
docker pull metabase
docker run -p 3000:3000 --name metabase metabase/metabase
```
Akses metabase pada http://localhost:3000/setup dan lakukan setup.

#### Setup Database (Supabase)
- Buat akun dan login https://supabase.com/dashboard/sign-in
- Copy URI pada database setting
- Buat new project
- Kirim dataset menggunakan sqlalchemy

```bash
from sqlalchemy import create_engine
 
URL = "DATABASE_URL"
    
engine = create_engine(URL)
df.to_sql('employee_data', engine, if_exists='replace')
```

#### Menjalankan Model Prediksi
```bash
python predict.py
```


## Business Dashboard

Dashboard HR yang dikembangkan memberikan pandangan menyeluruh tentang faktor-faktor yang mempengaruhi keluarnya karyawan di Jaya Jaya Maju. Dashboard ini memiliki beberapa bagian utama:

- __Executive Summary__: Menampilkan tingkat attrition keseluruhan dan distribusi karyawan yang bertahan vs keluar
- __Analisis Departemen__: Visualisasi attrition berdasarkan departemen
- __Analisis Demografis__: Menyoroti pola berdasarkan usia, status pernikahan, dan gender
- __Faktor Kepuasan Kerja__: Menganalisis hubungan antara kepuasan kerja dan attrition
- __Dampak Lembur dan Gaji__: Mengukur efek lembur dan tingkat gaji terhadap keputusan karyawan untuk keluar


## Temuan Utama

1. Tingkat Attrition Keseluruhan

    - Tingkat attrition saat ini: 16,92%
    - Total 1.058 karyawan, dengan 83% bertahan dan 17% telah keluar
    - Angka ini melebihi rata-rata industri yang sehat (10-12%), menunjukkan masalah serius yang perlu ditangani


2. Faktor-Faktor yang Mempengaruhi Attrition
    
    __Lembur (Overtime)__
    - Karyawan yang melakukan lembur memiliki tingkat attrition hampir tiga kali lebih tinggi dibandingkan dengan yang tidak lembur
    - Di semua departemen, karyawan dengan lembur konsisten menunjukkan kecenderungan lebih tinggi untuk keluar

    __Status Pernikahan__
    - Karyawan single/lajang menunjukkan tingkat attrition tertinggi, sementara karyawan yang sudah menikah memiliki tingkat attrition lebih rendah
    - Hal ini menunjukkan kemungkinan adanya perbedaan prioritas dan komitmen antara karyawan dengan status pernikahan berbeda

    __Kelompok Usia__
    - Karyawan muda (di bawah 25 tahun) dan karyawan dalam kelompok usia 25-34 menunjukkan tingkat attrition tertinggi
    - Karyawan yang lebih senior (35+ tahun) cenderung lebih setia pada perusahaan

    __Tingkat Gaji__
    - Terdapat korelasi negatif yang jelas antara tingkat gaji dan attrition
    - Karyawan dengan gaji rendah dan menengah-bawah memiliki tingkat attrition tertinggi
    - Gaji tinggi terbukti efektif dalam mempertahankan karyawan


3. Analisis Departemen dan Peran Kerja
    * Departemen Research & Development memiliki jumlah karyawan terbanyak tetapi juga tingkat attrition yang signifikan
    * Departemen Sales menunjukkan persentase attrition tertinggi dibandingkan departemen lainnya
    * Departemen Human Resources memiliki jumlah karyawan paling sedikit dan tingkat attrition moderat


4. Kepuasan Kerja dan Masa Kerja
    * Kepuasan kerja berkorelasi kuat dengan retensi - karyawan dengan tingkat kepuasan "Tinggi" dan "Sangat Tinggi" memiliki tingkat attrition jauh lebih rendah
    * Periode kritis untuk attrition terjadi pada:
        + Tahun pertama karyawan bekerja
        + Periode 2-3 tahun masa kerja
        + Periode 6-7 tahun masa kerja


## Rekomendasi Action Items

Berdasarkan analisis komprehensif data karyawan Jaya Jaya Maju, berikut adalah rekomendasi strategis untuk mengurangi tingkat attrition:

1. Manajemen Lembur yang Lebih Baik
    - Implementasikan sistem pemantauan lembur untuk mengidentifikasi karyawan yang sering bekerja melebihi jam kerja normal
    - Distribusikan beban kerja secara lebih merata di antara tim untuk mengurangi kebutuhan lembur
    - Pertimbangkan untuk menambah staf di departemen dengan kebutuhan lembur tinggi
    - Berikan kompensasi atau waktu istirahat yang memadai untuk lembur yang tidak dapat dihindari

2. Program Dukungan Berdasarkan Demografi
    - Kembangkan program retensi khusus untuk karyawan muda dan belum menikah, seperti:
        - Peluang pengembangan karir yang jelas
        - Program mentoring dan pelatihan
        - Kegiatan sosial dan pembentukan komunitas di tempat kerja
    - Desain kebijakan kerja fleksibel yang mendukung keseimbangan kehidupan-kerja, terutama untuk karyawan dengan berbagai situasi keluarga

3.  Strategi Kompensasi Bertingkat
    - Evaluasi struktur gaji saat ini dan sesuaikan untuk memastikan kompetitif di pasar
    - Implementasikan peningkatan gaji yang lebih sering untuk karyawan berkinerja tinggi
    - Kembangkan paket benefit yang disesuaikan dengan kebutuhan karyawan di berbagai tahap karir
    - Berikan insentif retensi untuk posisi-posisi kritis dan sulit diisi

4. Intervensi Departemen Spesifik
    - Sales: Tinjau target penjualan dan struktur insentif untuk memastikan realistis dan memotivasi
    - Research & Development: Ciptakan jalur karir teknis yang lebih jelas dan peluang pengembangan keahlian
    - Human Resources: Tingkatkan dukungan untuk tim HR agar dapat lebih efektif mendukung departemen lain

5. Program Peningkatan Kepuasan Kerja
    - Lakukan survei engagement karyawan secara rutin untuk mengidentifikasi area yang perlu perbaikan
    - Implementasikan program pengakuan dan penghargaan untuk meningkatkan moral
    - Tingkatkan komunikasi manajemen-karyawan dan transparansi pengambilan keputusan
    - Berikan peluang untuk pengembangan profesional dan pembelajaran berkelanjutan

6. Perhatian pada Tahun-Tahun Kritis
    - Desain program onboarding yang kuat untuk karyawan baru untuk meningkatkan retensi tahun pertama
    - Buat intervensi khusus untuk karyawan yang mendekati masa kerja 2-3 tahun dan 6-7 tahun
    - Lakukan wawancara "stay" secara berkala untuk mengidentifikasi masalah sebelum menyebabkan karyawan mempertimbangkan untuk keluar


## Kesimpulan

Tingkat attrition 16,92% di Jaya Jaya Maju menunjukkan kebutuhan mendesak untuk intervensi strategis. Dengan implementasi rekomendasi di atas, perusahaan memiliki peluang signifikan untuk meningkatkan retensi karyawan, mengurangi biaya rekrutmen dan pelatihan, serta meningkatkan stabilitas dan produktivitas operasional. Dashboard analitik yang telah dikembangkan akan menjadi alat penting untuk memantau efektivitas intervensi ini dan membuat keputusan berbasis data dalam pengelolaan sumber daya manusia ke depannya.

Model machine learning yang telah dikembangkan juga dapat digunakan untuk identifikasi dini karyawan berisiko tinggi keluar, memungkinkan tindakan proaktif sebelum keputusan untuk keluar dibuat. Dengan pendekatan holistik ini, Jaya Jaya Maju dapat mentransformasi tantangan attrition menjadi peluang untuk memperkuat budaya organisasi dan meningkatkan kepuasan karyawan secara keseluruhan.


Username: root@mail.com
Password: root123