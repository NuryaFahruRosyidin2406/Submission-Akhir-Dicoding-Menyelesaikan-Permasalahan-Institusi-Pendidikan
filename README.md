# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech - Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu perguruan ternama yang telah berdiri sejak tahun 2000 dan memiliki reputasi tinggi dalam mencetak lulusan berkualitas. Namun, institusi ini menghadapi tantangan besar terkait tingginya angka *dropout* (putus kuliah) di kalangan mahasiswa. 

Tingginya tingkat *dropout* tidak hanya berdampak negatif pada reputasi institusi, tetapi juga memengaruhi keberlangsungan finansial dan efektivitas operasional pendidikan. Untuk mengatasi masalah ini, Jaya Jaya Institut ingin menerapkan pendekatan berbasis data (*data-driven approach*) guna mendeteksi mahasiswa yang berisiko mengalami *dropout* sedini mungkin, sehingga intervensi dan bimbingan khusus dapat diberikan sebelum terlambat. Selain itu, pihak manajemen membutuhkan visualisasi data yang mudah dipahami untuk memantau performa mahasiswanya.

### Permasalahan Bisnis
Saat ini, Jaya Jaya Institut menghadapi masalah tingginya angka *dropout* mahasiswa yang cukup signifikan. Tingginya angka *dropout* ini menimbulkan kerugian finansial bagi institusi akibat kehilangan potensi pendapatan UKT/SPP serta penurunan efisiensi alokasi sumber daya operasional pendidikan. 

Selain dampak finansial, tingginya angka *dropout* berisiko menurunkan reputasi akademis Jaya Jaya Institut di mata publik dan calon mahasiswa baru, yang dalam jangka panjang dapat menurunkan daya saing institusi. Ketiadaan sistem deteksi dini menyebabkan pihak manajemen dan dosen pembimbing terlambat memberikan intervensi atau bimbingan khusus kepada mahasiswa yang sedang mengalami kesulitan akademis maupun non-akademis. Jika permasalahan ini dibiarkan tanpa tindakan preventif, Jaya Jaya Institut berisiko kehilangan calon-calon lulusan berpotensi dan menghambat pertumbuhan serta keberlanjutan institusi.

### Pertanyaan Bisnis
Untuk menjawab permasalahan bisnis tersebut, proyek ini akan menjawab beberapa pertanyaan analisis utama sebagai berikut:

1. Berapa banyak mahasiswa yang saat ini statusnya *Dropout*, *Enrolled* (masih aktif), dan *Graduate* (lulus) di Jaya Jaya Institut?
2. Seberapa besar pengaruh jumlah mata kuliah yang lulus (`approved`) dan rata-rata nilai (`grade`) di semester 1 dan 2 terhadap risiko mahasiswa *dropout*?
3. Apakah masalah keuangan seperti punya tunggakan (`Debtor`) atau terlambat bayar SPP (`Tuition_fees_up_to_date`) menjadi alasan utama mahasiswa berhenti kuliah atau *dropout*?
4. Seberapa efektif program beasiswa (`Scholarship_holder`) dalam mencegah dan menekan angka *dropout* mahasiswa?
5. Apakah faktor usia saat masuk (`Age_at_enrollment`), jenis kelamin, atau status pernikahan membuat mahasiswa lebih rawan mengalami *dropout*?
6. Apakah kondisi ekonomi luar (seperti tingkat pengangguran, inflasi, dan GDP) ikut memengaruhi keputusan mahasiswa untuk berhenti kuliah?
7. Seperti apa profil atau ciri-ciri mahasiswa yang paling berisiko *dropout* berdasarkan karakteristik akademis, finansial, dan demografi, agar tim kemahasiswaan bisa cepat memberikan bimbingan khusus?

### Cakupan Proyek
Proyek ini mencakup alur kerja analisis data pendidikan secara end-to-end dengan batasan proses dan output akhir sebagai berikut:

* **Eksplorasi & Pembersihan Data:** Memproses dan membersihkan dataset performa mahasiswa (*students' performance*) yang mencakup 36 fitur (demografi, latar belakang akademis, sosio-ekonomi, indikator akademis semester 1 & 2, serta makroekonomi) dan 1 variabel target (`Status`) untuk memastikan kualitas data yang siap dianalisis.
* **Penyimpanan Data (Data Warehouse):** Mengonfigurasi dan memuat dataset yang telah dibersihkan ke dalam database PostgreSQL di Supabase.
* **Analisis Data & Formulasi Strategi:** Menganalisis pola *dropout* pada berbagai segmen (seperti tingkat kelulusan mata kuliah semester awal, status pembayaran SPP, status beasiswa, dan latar belakang sosio-ekonomi) untuk mengidentifikasi pemicu utama kegagalan studi.
* **Pengembangan Business Dashboard:** Merancang dan membangun dashboard visualisasi data interaktif menggunakan **Metabase** untuk memantau metrik utama performa mahasiswa serta memetakan faktor risiko *dropout*.
* **Pengembangan & Deploy Model Machine Learning:** Membangun dan mengevaluasi model klasifikasi Machine Learning (memprediksi status `Dropout`, `Enrolled`, `Graduate`) siap pakai untuk memprediksi risiko *dropout* secara presisi, lalu mengintegrasikan prototipe model ke dalam aplikasi **Streamlit** .
* **Output Akhir:**
  1. Database terstruktur di Supabase.
  2. Business Dashboard interaktif di Metabase.
  3. Model Machine Learning siap pakai (*trained model*).
  4. Prototype aplikasi interaktif di Streamlit Community Cloud.
  5. Laporan analisis komprehensif.
  6. **Saran rekomendasi *action items*** untuk membantu Jaya Jaya Institut memberikan bimbingan khusus dan menekan angka *dropout*.

### Persiapan
#### **Sumber data:** Dataset *students_performance* di Jaya Jaya Institut ('data.csv') yang mencakup variabel demografi mahasiswa, latar belakang pendidikan & orang tua, status finansial/beasiswa, performa akademik semester 1 dan 2, indikator sosio-ekonomi, serta status kelulusan mahasiswa (*Status*: Graduate, Dropout, Enrolled). Tautan dataset dapat diakses melalui [Link Dataset](https://github.com/NuryaFahruRosyidin2406/Submission-Akhir-Dicoding-Menyelesaikan-Permasalahan-Institusi-Pendidikan/tree/main/Dataset/students_performance).

#### **Setup environment**:
Berikut ini adalah panduan dalam menyiapkan environment

* **Prerequisites & Versions**
   1. **Python Version:** `3.13.7`
   2. **Metabase Version:** `v0.63.16.9`
   3. **Miniconda Version:** `26.7.1`

#### 1. Eksplorasi Data & Pemrosesan Awal (Google Colab)
1. Buka berkas `notebook.ipynb` di [Google Colab](https://colab.research.google.com/).
2. Unggah file `requirements.txt` ke direktori kerja Colab (panel *Files* di sebelah kiri).
3. Jalankan sel pertama untuk menginstal seluruh dependensi:
   ```bash
   !pip install -r requirements.txt
   ```

#### 2. Konfigurasi Dashboard Metabase (Local Machine via Docker)
1. Jalankan Container Metabase (Pertama Kali):

    Buka Terminal / Command Prompt, lalu jalankan perintah:

    ```bash
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```

2. Menjalankan Kembali Container yang Sudah Ada:

    Jika container sudah pernah dibuat sebelumnya, jalankan:

    ```bash
    docker start metabase
    ```

3. Akses & Hubungkan ke Supabase:

    * Buka peramban (browser) dan akses http://localhost:3000.

    * Hubungkan Metabase ke PostgreSQL Supabase menggunakan kredensial database proyek.

#### 3. Pengolahan Lokal & Aplikasi Streamlit (Anaconda / Miniconda)
1. Buka Terminal / Anaconda Prompt dan buat environment baru:

    ```bash
    conda create -n jaya-jaya-env python=3.11 -y
    ```

2. Aktifkan Environment:

    ```bash
    conda activate jaya-jaya-env
    ```

3. Clone Repository & Install Dependensi:

    ```bash
    git clone [https://github.com/username/repository-kamu.git](https://github.com/username/repository-kamu.git)
    cd repository-kamu
    pip install -r requirements.txt
    ```

4. Menjalankan Aplikasi Streamlit Lokal:

    ```bash
    streamlit run app.py
    ```

#### 4. Deployment Aplikasi Online (Streamlit Community Cloud)
Aplikasi prototype ini juga di-deploy secara online menggunakan file modular data_preprocessing.py, prediction.py, dan app.py:

1. Push seluruh perubahan file beserta requirements.txt ke repositori GitHub.

2. Buka share.streamlit.io dan hubungkan dengan repositori GitHub proyek.

3. Pastikan memilih Python 3.11 pada menu App Settings.

## Business Dashboard
Dashboard Student Performance & Dropout Analytics ini dikembangkan menggunakan **Metabase** untuk memantau tingkat kelulusan serta mengidentifikasi faktor-faktor risiko yang menyebabkan mahasiswa berhenti kuliah (*dropout*) di Jaya Jaya Institut. Desain visual menggunakan pendekatan *dark theme* dengan skema warna intuitif (hijau untuk mahasiswa lulus, biru untuk mahasiswa aktif, dan merah untuk indikator risiko *dropout*) agar *data storytelling* tersampaikan dengan jelas.

Dashboard ini terbagi menjadi lima area analisis utama, yaitu:
1. **Gambaran Umum & Performa Akademik:** Ini menampilkan KPI populasi mahasiswa berdasarkan status akhir (Graduate, Enrolled, Dropout) serta menguraikan korelasi antara capaian SKS lulus dan rerata nilai pada semester 1 dan 2 terhadap risiko *dropout*.
2. **Analisis Keuangan & Beasiswa:** Ini mengidentifikasi hubungan antara masalah finansial (kelancaran SPP dan status tunggakan hutang) serta efektivitas program beasiswa dalam menekan angka *dropout* mahasiswa.
3. **Profil Demografi & Faktor Sosial:** Ini menganalisis dampak usia saat mendaftar, jenis kelamin, dan status pernikahan terhadap tingkat kerentanan mahasiswa mengalami putus studi.
4. **Indikator Lingkungan Ekonomi Makro:** Ini memantau pengaruh tren kondisi ekonomi luar seperti tingkat pengangguran, inflasi, dan pertumbuhan GDP terhadap keputusan mahasiswa untuk melanjutkan atau menghentikan perkuliahan.
5. **Profil Risiko Mahasiswa:** Ini memetakan matriks risiko berdasarkan capaian SKS awal, kombinasi status finansial-beasiswa, dan kelompok usia untuk membantu tim kemahasiswaan supaya bisa cepat memberikan bimbingan khusus.

**Link Dashboard:** [Link Metabase di Sini]

## Menjalankan Sistem Machine Learning
Prototype sistem *machine learning* ini dikembangkan menggunakan *framework* Streamlit untuk memprediksi risiko *dropout* mahasiswa Jaya-Jaya Institut.

### 1. Menjalankan Secara Lokal (Local Environment)
Sebelum menjalankan aplikasi secara lokal, pastikan seluruh dependensi telah terpasang (lihat bagian *Setup Environment*). Kemudian jalankan perintah berikut di terminal:

```bash
streamlit run app.py
```

Setelah perintah dijalankan, browser akan otomatis membuka antarmuka aplikasi pada alamat lokal http://localhost:8501.

### 2. Mengakses Prototype Streamlit Online (Cloud Deployment)
Sistem prototype yang di deploy ke Streamlit Community Cloud dapat diakses secara langsung tanpa perlu melakukan instalasi lokal. Berikut ini adalah tautan link untuk mengakses Prototype Streamlit Online [https://jaya-jaya-institute-dropout-prediction.streamlit.app](https://jaya-jaya-institute-dropout-prediction.streamlit.app)

## Conclusion
Berdasarkan hasil analisis data dan visualisasi pada **Jaya Jaya Institut - Student Performance & Dropout Analytics Dashboard**, berikut ini ada beberapa kesimpulan yang dapat diambil, seperti:

### 1. Gambaran Umum & Distribusi Status Mahasiswa
* Dari total **4.424 mahasiswa** yang terdata, sebanyak **1.421 mahasiswa** berstatus **Dropout**, **794 mahasiswa** berstatus **Enrolled** (masih aktif), dan **2.209 mahasiswa** berhasil **Graduate** (lulus).
* Angka *dropout* ini tergolong tinggi dan berdampak langsung pada potensi kehilangan pendapatan SPP/UKT serta efisiensi operasional institusi.

### 2. Faktor Pemicu Utama & Profil Karakteristik Mahasiswa Berisiko Dropout
* **Faktor Akademis:** Performa semester 1 dan 2 menjadi prediktor paling krusial. Mahasiswa *dropout* rata-rata hanya lulus **2,55 MK (Semester 1)** dan **1,94 MK (Semester 2)** dengan rerata nilai **7,26** dan **5,90**. Angka ini jauh di bawah mahasiswa yang lulus (*Graduate*), yang rata-rata menyelesaikan **> 6 MK** per semester dengan rata-rata nilai **> 12,6**.
* **Faktor Finansial & SPP:** Kelancaran pembayaran SPP sangat memengaruhi keberlanjutan studi. Sebanyak **457 dari 528 mahasiswa yang menunggak SPP** berakhir *dropout*. Sebaliknya, mahasiswa yang lancar membayar SPP mayoritas berhasil lulus (2.180 mahasiswa).
* **Efektivitas Beasiswa:** Program beasiswa terbukti sangat efektif menekan angka putus kuliah. Dari **1.099 penerima beasiswa**, sebanyak **835 orang** berhasil lulus dan hanya **134 orang** yang *dropout*. Sementara pada kelompok non-beasiswa, angka *dropout* melonjak hingga **1.287 dari 3.325 mahasiswa**.
* **Demografi (Usia Masuk, Gender, & Status Pernikahan):**
  * **Usia Masuk:** Mahasiswa yang mendaftar pada usia lebih matang (**> 30 tahun**) memiliki proporsi *dropout* tertinggi, yaitu **355 dari 662 mahasiswa**, diikuti kelompok usia **25–30 tahun (276 dari 476 mahasiswa)**.
  * **Jenis Kelamin:** Mahasiswa **Laki-laki** memiliki rasio *dropout* lebih tinggi (**701 dari 1.556 total mahasiswa laki-laki**) dibandingkan mahasiswa **Perempuan** (**720 dari 2.868 total mahasiswa perempuan**).
  * **Status Pernikahan:** Mahasiswa dengan status menikah atau pernah menikah (bercerai/berpisah) menunjukkan persentase *dropout* yang signifikan lebih rendah dibanding yang belum menikah.
* **Kondisi Makroekonomi:** Tingkat pengangguran dan inflasi relatif stabil pada ketiga kelompok status mahasiswa. Namun, tren **GDP yang negatif (-0,15)** berasosiasi dengan kelompok mahasiswa *dropout*, ini mengindikasikan bahwa penurunan kondisi ekonomi makro dapat berpotensi mengganggu stabilitas finansial keluarga/mahasiswa.

### 3. Matriks Kombinasi Risiko Kritis
Terdapat **267 mahasiswa** (dropout) yang berada di zona risiko paling tinggi (*critical zone*), yaitu mahasiswa yang **memiliki tunggakan SPP sekaligus lulus kurang dari 3 mata kuliah di semester 1**. Selain itu, mahasiswa yang **tidak menerima beasiswa dan menunggak SPP** mencatatkan angka *dropout* sekitar **429 mahasiswa**.

### Rekomendasi Action Items
Berdasarkan temuan data pada dashboard dan hasil prediksi model, berikut ini ada beberapa rekomendasi aksi strategis berbasis data untuk dapat menekan angka *dropout* di Jaya Jaya Institut:

### 1. Sistem Peringatan Dini & Intervensi Akademis Semester Awal (Prioritas 1)
* **Insight Data:** Mahasiswa *dropout* mengalami penurunan drastis dalam kelulusan MK sejak Semester 1 hingga Semester 2.
* **Aksi Strategis:**
  * Mengintegrasikan aplikasi prediksi berbasis Machine Learning (Streamlit) ke dalam sistem akademik kampus untuk mendeteksi mahasiswa yang berisiko tinggi untuk *dropout* sebelum semester berjalan usai.
  * Mewajibkan atau mengadakan program bimbingan/konseling akademik dan kelas belajar bareng bagi mahasiswa yang lulus **< 3 MK** pada evaluasi pertengahan/akhir Semester 1.

### 2. Skema Bantuan Finansial & Fleksibilitas Pembayaran SPP (Prioritas 2)
* **Insight Data:** Sebanyak **457 mahasiswa** mahasiswa yang menunggak SPP berakhir *dropout*, dan kelompok non-beasiswa menyumbang *dropout* terbanyak (1.287 mahasiswa).
* **Aksi Strategis:**
  * Memberikan fasilitas skema cicilan pembayaran SPP atau penundaan pembayaran berbasis permohonan bagi mahasiswa yang berdampak finansial.
  * Dialokasikannya sebagian anggaran beasiswa secara khusus bagi mahasiswa aktif (*Enrolled*) yang berprestasi atau berisiko *dropout* akibat kendala finansial mendadak.

### 3. Program Pendampingan Khusus Mahasiswa Usia Dewasa & Non-Reguler (Prioritas 3)
* **Insight Data:** Mahasiswa yang masuk di usia **> 25 tahun** memiliki tingkat *dropout* yang juga tinggi.
* **Aksi Strategis:**
  * Menyediakan layanan kelas fleksibel (*hybrid/online learning*) atau jadwal konsultasi malam/akhir pekan bagi mahasiswa pendaftar usia dewasa yang memiliki komitmen kerja atau keluarga.
  * Membentuk program komunitas bimbingan khusus untuk membantu mahasiswa non-reguler beradaptasi kembali dengan ritme perkuliahan.