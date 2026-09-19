# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech - Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu perguruan ternama yang telah berdiri sejak tahun 2000 dan memiliki reputasi tinggi dalam mencetak lulusan berkualitas. Namun, institusi ini menghadapi tantangan besar terkait tingginya angka *dropout* (putus kuliah) di kalangan mahasiswa. 

Tingginya tingkat *dropout* tidak hanya berdampak negatif pada reputasi institusi, tetapi juga memengaruhi keberlangsungan finansial dan efektivitas operasional pendidikan. Untuk mengatasi masalah ini, Jaya Jaya Institut ingin menerapkan pendekatan berbasis data (*data-driven approach*) guna mendeteksi mahasiswa yang berisiko mengalami *dropout* sedini mungkin, sehingga intervensi dan bimbingan khusus dapat diberikan sebelum terlambat. Selain itu, pihak manajemen membutuhkan visualisasi data yang mudah dipahami untuk memantau performa mahasiswanya.

### Permasalahan Bisnis
Saat ini, Jaya Jaya Institut menghadapi masalah tingginya angka *dropout* mahasiswa yang cukup signifikan. Tingginya angka *dropout* ini menimbulkan kerugian finansial bagi institusi akibat kehilangan potensi pendapatan UKT/SPP serta penurunan efisiensi alokasi sumber daya operasional pendidikan. 

Selain dampak finansial, tingginya angka *dropout* berisiko menurunkan reputasi akademis Jaya Jaya Institut di mata publik dan calon mahasiswa baru, yang dalam jangka panjang dapat menurunkan daya saing institusi. Ketiadaan sistem deteksi dini menyebabkan pihak manajemen dan dosen pembimbing terlambat memberikan intervensi atau bimbingan khusus kepada mahasiswa yang sedang mengalami kesulitan akademis maupun non-akademis. Jika permasalahan ini dibiarkan tanpa tindakan preventif, Jaya Jaya Institut berisiko kehilangan calon-calon lulusan berpotensi dan menghambat pertumbuhan serta keberlanjutan institusi.

### Pertanyaan Bisnis
Untuk menjawab permasalahan bisnis tersebut, proyek ini akan menjawab beberapa pertanyaan analisis utama sebagai berikut:

1. Berapa proporsi dan tingkat distribusi status mahasiswa (*Dropout*, *Enrolled*, dan *Graduate*) saat ini di Jaya Jaya Institut?
2. Bagaimana pengaruh indikator akademis semester awal (seperti jumlah unit mata kuliah yang disetujui/`approved`, jumlah evaluasi, serta rata-rata nilai semester 1 dan 2) terhadap risiko *dropout* mahasiswa?
3. Sejauh mana faktor finansial dan bantuan studi (seperti status tunggakan uang kuliah/`Debtor`, kelancaran pembayaran SPP/`Tuition fees up to date`, dan status penerima beasiswa/`Scholarship holder`) memengaruhi keputusan mahasiswa untuk bertahan atau *dropout*?
4. Apakah faktor demografi dan latar belakang pendaftaran (seperti usia saat mendaftar/`Age at enrollment`, gender, status pernikahan, status perantau/`Displaced`, jalur masuk/`Application mode`, serta tingkat pendidikan/pekerjaan orang tua) memiliki korelasi signifikan dengan tingkat keberhasilan studi?
5. Apakah kondisi makroekonomi (seperti `Unemployment rate`, `Inflation rate`, dan `GDP`) turut memengaruhi dinamika *dropout* mahasiswa?
6. Profil atau segmen mahasiswa seperti apa yang memiliki risiko *dropout* paling tinggi sehingga memerlukan bimbingan dan intervensi khusus sedini mungkin?

### Cakupan Proyek
Proyek ini mencakup alur kerja analisis data pendidikan secara end-to-end dengan batasan proses dan output akhir sebagai berikut:

* **Eksplorasi & Pembersihan Data:** Memproses dan membersihkan dataset performa mahasiswa (*students' performance*) yang mencakup 36 fitur (demografi, latar belakang akademis, sosio-ekonomi, indikator akademis semester 1 & 2, serta makroekonomi) dan 1 variabel target (`Target`) untuk memastikan kualitas data yang siap dianalisis.
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

Sumber data: ....

**Sumber data:** Dataset internal karyawan Jaya Jaya Maju ('employee_data.csv') yang mencakup variabel demografi, kepuasan kerja, kompensasi, jam kerja, dan status *attrition*. Tautan dataset dapat diakses melalui [Link Dataset](https://github.com/NuryaFahruRosyidin2406/Submission-Pertama-Menyelesaikan-Permasalahan-Human-Resources_Dicoding/tree/4b2219c75eeb4c7201a9da81ade9dd361f26bdb8/Dataset).

Setup environment:
```

```

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
