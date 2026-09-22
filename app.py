import streamlit as st
import pandas as pd
from data_preprocessing import data_preprocessing
from prediction import prediction

# ---------------------------------------------------------
# 1. KONFIGURASI HALAMAN STREAMLIT
# ---------------------------------------------------------
st.set_page_config(
    page_title="Jaya Jaya Institut - Student Outcome Prediction",
    page_icon="🎓",
    layout="wide",
)

# Header Utama
col1, col2 = st.columns([1, 5])
with col1:
    st.image(
        "https://raw.githubusercontent.com/NuryaFahruRosyidin2406/Submission-Akhir-Dicoding-Menyelesaikan-Permasalahan-Institusi-Pendidikan/main/assets/logo_topi_pensil-removebg-preview.png",
        width=120,
    )
with col2:
    st.title("Jaya Jaya Institut 🎓")
    st.subheader("Sistem Prediksi Kelulusan & Identifikasi Mahasiswa Dropout")

st.markdown("---")

# Sidebar - Informasi Aplikasi
st.sidebar.header("Detail Model ML")
st.sidebar.info(
    """
    **Model Utama**: Logistic Regression / Gradient Boosting  
    **Reduksi Dimensi**: PCA (22 Komponen)  
    **Target Status**:
    - **Dropout**: Mahasiswa putus studi
    - **Enrolled**: Mahasiswa aktif
    - **Graduate**: Mahasiswa lulus
    """
)

# ---------------------------------------------------------
# 2. MENU UTAMA (TABS INPUT DATA)
# Tab Kiri: Unggah CSV | Tab Kanan: Input Manual
# ---------------------------------------------------------
tab1, tab2 = st.tabs(["📁 Unggah CSV (Prediksi Masal)", "📝 Input Manual (Prediksi Tunggal)"])

# =========================================================
# TAB 1 (KIRI): UNGGAH CSV (MASS UPLOAD)
# =========================================================
with tab1:
    st.write("### 📁 Unggah Data Mahasiswa Masal (.csv)")

    # Petunjuk Penggunaan CSV & Keterangan Kode
    with st.expander("📖 Petunjuk Format Berkas CSV & Kode Enkodifikasi Data", expanded=True):
        st.markdown(
            """
            **Ketentuan Format File:**
            * File berformat **.csv** menggunakan pemisah titik koma (`;`) atau koma (`,`).
            * Memiliki 36 kolom fitur mentah sesuai format dataset utama.

            #### 🔍 Glosarium Panduan Nilai Input (Encoding Reference):
            * **Marital_status**: `1`: Single, `2`: Married, `3`: Widower, `4`: Divorced, `5`: Facto Union, `6`: Legally Separated
            * **Gender**: `1`: Male (Laki-laki), `0`: Female (Perempuan)
            * **Daytime_evening_attendance**: `1`: Daytime (Siang), `0`: Evening (Malam)
            * **Displaced / Educational_special_needs / Debtor / Tuition_fees_up_to_date / Scholarship_holder / International**: `1`: Ya, `0`: Tidak
            * **Course (Kode Jurusan)**: `9119`: Informatics, `9147`: Management, `9254`: Tourism, `9500`: Nursing, `9238`: Social Service, `9773`: Journalism, `171`: Design, `9003`: Agronomy
            """
        )

        # Template CSV Siap Unduh
        sample_dict = {
            "Marital_status": [1], "Application_mode": [1], "Application_order": [1], "Course": [9254],
            "Daytime_evening_attendance": [1], "Previous_qualification": [1], "Previous_qualification_grade": [122.0],
            "Nacionality": [1], "Mothers_qualification": [1], "Fathers_qualification": [1], "Mothers_occupation": [1],
            "Fathers_occupation": [1], "Admission_grade": [127.3], "Displaced": [1], "Educational_special_needs": [0],
            "Debtor": [0], "Tuition_fees_up_to_date": [1], "Gender": [1], "Scholarship_holder": [0],
            "Age_at_enrollment": [20], "International": [0], "Curricular_units_1st_sem_credited": [0],
            "Curricular_units_1st_sem_enrolled": [6], "Curricular_units_1st_sem_evaluations": [6],
            "Curricular_units_1st_sem_approved": [6], "Curricular_units_1st_sem_grade": [13.5],
            "Curricular_units_1st_sem_without_evaluations": [0], "Curricular_units_2nd_sem_credited": [0],
            "Curricular_units_2nd_sem_enrolled": [6], "Curricular_units_2nd_sem_evaluations": [6],
            "Curricular_units_2nd_sem_approved": [6], "Curricular_units_2nd_sem_grade": [12.8],
            "Curricular_units_2nd_sem_without_evaluations": [0], "Unemployment_rate": [10.8],
            "Inflation_rate": [1.4], "GDP": [1.74],
        }
        df_sample = pd.DataFrame(sample_dict)
        csv_sample_bytes = df_sample.to_csv(index=False, sep=";").encode("utf-8")

        st.download_button(
            label="📥 Unduh Contoh Template CSV",
            data=csv_sample_bytes,
            file_name="template_data_mahasiswa.csv",
            mime="text/csv",
        )

    uploaded_file = st.file_uploader("Pilih berkas CSV", type=["csv"], key="csv_uploader")

    if uploaded_file is not None:
        try:
            df_raw = pd.read_csv(uploaded_file, sep=";")
        except Exception:
            uploaded_file.seek(0)
            df_raw = pd.read_csv(uploaded_file, sep=",")

        if "Status" in df_raw.columns:
            df_features = df_raw.drop(columns=["Status"])
        else:
            df_features = df_raw.copy()

        with st.expander("👁️ Lihat Preview Data Mentah"):
            st.dataframe(df_raw.head(10), use_container_width=True)

        if "df_result" not in st.session_state:
            st.session_state.df_result = None
        if "preds" not in st.session_state:
            st.session_state.preds = None

        if st.button("🚀 Jalankan Prediksi Masal", type="primary"):
            with st.spinner("Memproses preprocessing data & menjalankan prediksi..."):
                df_preprocessed = data_preprocessing(data=df_features)
                preds = prediction(data=df_preprocessed)

                df_result = df_raw.copy()
                
                # Memindahkan kolom Hasil_Prediksi ke Urutan Paling Depan (Paling Kiri)
                df_result.insert(0, "Hasil_Prediksi", preds)

                st.session_state.df_result = df_result
                st.session_state.preds = preds

        if st.session_state.df_result is not None:
            st.success("✅ Prediksi Berhasil Diselesaikan!")

            st.write("### 📊 Ringkasan Hasil Prediksi")
            col_res1, col_res2, col_res3 = st.columns(3)
            counts = pd.Series(st.session_state.preds).value_counts()

            with col_res1:
                st.metric("Total Graduate", counts.get("Graduate", 0))
            with col_res2:
                st.metric("Total Enrolled", counts.get("Enrolled", 0))
            with col_res3:
                st.metric("Total Dropout", counts.get("Dropout", 0))

            st.write("### 📋 Detail Hasil Prediksi Mahasiswa")
            st.caption("📌 Kolom **Hasil_Prediksi** dan informasi kunci diletakkan di paling depan serta dikonversi ke format teks agar mudah dibaca.")

            # ---------------------------------------------------------
            # FORMATTING DATAFRAME TAMPILAN (USER-FRIENDLY)
            # ---------------------------------------------------------
            df_display = st.session_state.df_result.copy()

            # Mapping Nilai Angka ke Teks
            map_marital = {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced", 5: "Facto Union", 6: "Legally Separated"}
            map_gender = {0: "Female", 1: "Male"}
            map_binary = {0: "No", 1: "Yes"}
            map_course = {
                33: "Biofuel Production Tech", 171: "Animation & Multimedia Design", 8014: "Social Service (Evening)",
                9003: "Agronomy", 9070: "Communication Design", 9085: "Veterinary Nursing", 9119: "Informatics Engineering",
                9130: "Equinculture", 9147: "Management", 9238: "Social Service", 9254: "Tourism", 9500: "Nursing",
                9556: "Oral Hygiene", 9670: "Advertising & Marketing", 9773: "Journalism & Communication",
                9853: "Basic Education", 9991: "Management (Evening)"
            }

            # Terapkan Mapping jika Kolom Ada
            if "Marital_status" in df_display.columns:
                df_display["Marital_status"] = df_display["Marital_status"].map(map_marital).fillna(df_display["Marital_status"])
            if "Gender" in df_display.columns:
                df_display["Gender"] = df_display["Gender"].map(map_gender).fillna(df_display["Gender"])
            if "Course" in df_display.columns:
                df_display["Course"] = df_display["Course"].map(map_course).fillna(df_display["Course"])
            if "Tuition_fees_up_to_date" in df_display.columns:
                df_display["Tuition_fees_up_to_date"] = df_display["Tuition_fees_up_to_date"].map(map_binary).fillna(df_display["Tuition_fees_up_to_date"])
            if "Scholarship_holder" in df_display.columns:
                df_display["Scholarship_holder"] = df_display["Scholarship_holder"].map(map_binary).fillna(df_display["Scholarship_holder"])

            # Reorder Kolom Kunci ke Urutan Depan (Paling Kiri)
            priority_cols = ["Hasil_Prediksi", "Marital_status", "Gender", "Age_at_enrollment", "Course", "Tuition_fees_up_to_date", "Scholarship_holder"]
            existing_priority = [col for col in priority_cols if col in df_display.columns]
            remaining_cols = [col for col in df_display.columns if col not in existing_priority]
            
            df_display = df_display[existing_priority + remaining_cols]
            
            # Tampilkan Tabel
            st.dataframe(df_display, use_container_width=True)

            # Tombol Unduh & Reset
            col_btn1, col_btn2, _ = st.columns([1, 1, 2])
            csv_data = df_display.to_csv(index=False).encode("utf-8")

            with col_btn1:
                st.download_button(
                    label="📥 Unduh Hasil Prediksi (.csv)",
                    data=csv_data,
                    file_name="hasil_prediksi_mahasiswa.csv",
                    mime="text/csv",
                    type="secondary",
                    use_container_width=True,
                )

            with col_btn2:
                if st.button("🔄 Mau prediksi lagi?", type="primary", use_container_width=True):
                    st.session_state.df_result = None
                    st.session_state.preds = None
                    st.rerun()

    else:
        st.session_state.df_result = None
        st.session_state.preds = None
        st.info("Silakan unggah file CSV data mahasiswa di atas untuk memulai analisis prediksi.")


# =========================================================
# TAB 2 (KANAN): INPUT MANUAL (PREDIKSI TUNGGAL)
# =========================================================
with tab2:
    st.write("### Form Input Data Mahasiswa (Prediksi Tunggal)")
    
    # Petunjuk Pengisian Input Manual
    st.info(
        """
        💡 **Petunjuk Pengisian:**  
        Pilih atau masukkan data mahasiswa menggunakan opsi pilihan di bawah ini. 
        Anda tidak perlu memasukkan kode angka secara manual karena sistem akan otomatis mengonversi pilihan Anda.
        """
    )

    with st.form(key="single_pred_form"):
        col_f1, col_f2, col_f3 = st.columns(3)

        with col_f1:
            st.markdown("#### 👤 Demografi & Status")
            marital_opt = st.selectbox(
                "Status Pernikahan (Marital Status)",
                ["Single", "Married", "Widower", "Divorced", "Facto Union", "Legally Separated"],
                help="Pilih status pernikahan mahasiswa saat ini."
            )
            gender_opt = st.selectbox("Jenis Kelamin (Gender)", ["Female", "Male"])
            age = st.number_input("Usia saat Mendaftar (Age at Enrollment)", min_value=15, max_value=80, value=20, help="Masukkan umur mahasiswa saat pendaftaran.")
            nacionality_opt = st.selectbox("Kewarganegaraan", ["Portuguese", "Other / International"])
            disability_opt = st.selectbox("Kebutuhan Khusus (Educational Special Needs)", ["No", "Yes"])

        with col_f2:
            st.markdown("#### 🎓 Jalur Masuk & Finansial")
            course_opt = st.selectbox(
                "Program Studi (Course)",
                [
                    "Informatics Engineering",
                    "Management",
                    "Tourism",
                    "Nursing",
                    "Social Service",
                    "Journalism and Communication",
                    "Advertising and Marketing Management",
                    "Basic Education",
                    "Animation and Multimedia Design",
                    "Agronomy"
                ]
            )
            shift_opt = st.selectbox("Waktu Kuliah (Attendance)", ["Daytime", "Evening"])
            prev_qual_opt = st.selectbox(
                "Pendidikan Sebelumnya",
                ["Secondary Education", "Higher Education (Bachelor/Degree)", "Basic Education", "Technological Specialization Course"]
            )
            prev_grade = st.number_input("Nilai Pendidikan Sebelumnya", min_value=0.0, max_value=200.0, value=120.0, help="Skala nilai 0 sampai 200.")
            admission_grade = st.number_input("Nilai Ujian Masuk", min_value=0.0, max_value=200.0, value=125.0, help="Skala nilai 0 sampai 200.")
            debtor_opt = st.selectbox("Memiliki Tunggakan Biaya (Debtor)?", ["No", "Yes"])
            tuition_opt = st.selectbox("Uang Kuliah Lunas (Tuition Fees Up to Date)?", ["Yes", "No"])
            scholarship_opt = st.selectbox("Penerima Beasiswa (Scholarship Holder)?", ["No", "Yes"])

        with col_f3:
            st.markdown("#### 📚 Performa Akademik Semester 1 & 2")
            cu_1st_enrolled = st.number_input("Mata Kuliah Diambil (Sem 1)", min_value=0, max_value=30, value=6)
            cu_1st_approved = st.number_input("Mata Kuliah Lulus (Sem 1)", min_value=0, max_value=30, value=5)
            cu_1st_grade = st.number_input("Rata-rata Nilai Sem 1", min_value=0.0, max_value=20.0, value=12.5, help="Skala nilai 0 sampai 20.")

            cu_2nd_enrolled = st.number_input("Mata Kuliah Diambil (Sem 2)", min_value=0, max_value=30, value=6)
            cu_2nd_approved = st.number_input("Mata Kuliah Lulus (Sem 2)", min_value=0, max_value=30, value=5)
            cu_2nd_grade = st.number_input("Rata-rata Nilai Sem 2", min_value=0.0, max_value=20.0, value=12.0, help="Skala nilai 0 sampai 20.")

        submit_single = st.form_submit_button("🚀 Jalankan Prediksi", type="primary", use_container_width=True)

    if submit_single:
        # Kamus Pemetaan Opsi Teks ke Kode Numerik Berdasarkan README.md
        map_marital = {"Single": 1, "Married": 2, "Widower": 3, "Divorced": 4, "Facto Union": 5, "Legally Separated": 6}
        map_gender = {"Female": 0, "Male": 1}
        map_binary = {"No": 0, "Yes": 1}
        map_tuition = {"No": 0, "Yes": 1}
        map_shift = {"Evening": 0, "Daytime": 1}
        map_nacionality = {"Portuguese": 1, "Other / International": 41}
        map_prev_qual = {
            "Secondary Education": 1,
            "Higher Education (Bachelor/Degree)": 2,
            "Basic Education": 19,
            "Technological Specialization Course": 39
        }
        map_course = {
            "Informatics Engineering": 9119,
            "Management": 9147,
            "Tourism": 9254,
            "Nursing": 9500,
            "Social Service": 9238,
            "Journalism and Communication": 9773,
            "Advertising and Marketing Management": 9670,
            "Basic Education": 9853,
            "Animation and Multimedia Design": 171,
            "Agronomy": 9003
        }

        # Konstruksi DataFrame 36 Fitur Mentah
        input_dict = {
            "Marital_status": map_marital[marital_opt],
            "Application_mode": 1,
            "Application_order": 1,
            "Course": map_course[course_opt],
            "Daytime_evening_attendance": map_shift[shift_opt],
            "Previous_qualification": map_prev_qual[prev_qual_opt],
            "Previous_qualification_grade": prev_grade,
            "Nacionality": map_nacionality[nacionality_opt],
            "Mothers_qualification": 1,
            "Fathers_qualification": 1,
            "Mothers_occupation": 1,
            "Fathers_occupation": 1,
            "Admission_grade": admission_grade,
            "Displaced": 1,
            "Educational_special_needs": map_binary[disability_opt],
            "Debtor": map_binary[debtor_opt],
            "Tuition_fees_up_to_date": map_tuition[tuition_opt],
            "Gender": map_gender[gender_opt],
            "Scholarship_holder": map_binary[scholarship_opt],
            "Age_at_enrollment": age,
            "International": 1 if nacionality_opt != "Portuguese" else 0,
            "Curricular_units_1st_sem_credited": 0,
            "Curricular_units_1st_sem_enrolled": cu_1st_enrolled,
            "Curricular_units_1st_sem_evaluations": cu_1st_enrolled,
            "Curricular_units_1st_sem_approved": cu_1st_approved,
            "Curricular_units_1st_sem_grade": cu_1st_grade,
            "Curricular_units_1st_sem_without_evaluations": 0,
            "Curricular_units_2nd_sem_credited": 0,
            "Curricular_units_2nd_sem_enrolled": cu_2nd_enrolled,
            "Curricular_units_2nd_sem_evaluations": cu_2nd_enrolled,
            "Curricular_units_2nd_sem_approved": cu_2nd_approved,
            "Curricular_units_2nd_sem_grade": cu_2nd_grade,
            "Curricular_units_2nd_sem_without_evaluations": 0,
            "Unemployment_rate": 10.8,
            "Inflation_rate": 1.4,
            "GDP": 1.74,
        }

        df_single = pd.DataFrame([input_dict])

        with st.spinner("Memproses data & memprediksi..."):
            df_single_preprocessed = data_preprocessing(data=df_single)
            single_pred = prediction(data=df_single_preprocessed)[0]

        st.markdown("---")
        st.write("### 🎯 Hasil Prediksi Mahasiswa")
        if single_pred == "Dropout":
            st.error(f"⚠️ Hasil Prediksi: **{single_pred}** — Mahasiswa berisiko tinggi putus studi. Diperlukan intervensi akademik!")
        elif single_pred == "Enrolled":
            st.warning(f"ℹ️ Hasil Prediksi: **{single_pred}** — Mahasiswa berstatus aktif.")
        else:
            st.success(f"🎉 Hasil Prediksi: **{single_pred}** — Mahasiswa diperkirakan lulus tepat waktu.")