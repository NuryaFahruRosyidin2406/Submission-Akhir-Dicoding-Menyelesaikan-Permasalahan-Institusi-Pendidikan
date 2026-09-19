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

**Sumber data:** Dataset *students_performance* di Jaya Jaya Institut ('data.csv') yang mencakup variabel demografi mahasiswa, latar belakang pendidikan & orang tua, status finansial/beasiswa, performa akademik semester 1 dan 2, indikator sosio-ekonomi, serta status kelulusan mahasiswa (*Status*: Graduate, Dropout, Enrolled). Tautan dataset dapat diakses melalui [Link Dataset](https://github.com/NuryaFahruRosyidin2406/Submission-Akhir-Dicoding-Menyelesaikan-Permasalahan-Institusi-Pendidikan/tree/main/Dataset/students_performance).

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
