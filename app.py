import streamlit as st
import pandas as pd
from data_preprocessing import data_preprocessing
from prediction import prediction

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Jaya Jaya Institut - Student Outcome Prediction",
    page_icon="🎓",
    layout="wide",
)

# Header Utama
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://raw.githubusercontent.com/NuryaFahruRosyidin2406/Submission-Akhir-Dicoding-Menyelesaikan-Permasalahan-Institusi-Pendidikan/main/assets/logo_topi_pensil-removebg-preview.png", width=120)
with col2:
    st.title("Jaya Jaya Institut 🎓")
    st.subheader("Sistem Prediksi Kelulusan & Identifikasi Mahasiswa Dropout")

st.markdown("---")

# Sidebar - Informasi Aplikasi
st.sidebar.header("Detail Model ML")
st.sidebar.info(
    """
    **Model**: Logistic Regression  
    **Reduksi Dimensi**: PCA (22 Komponen)  
    **Target Status**:
    - **Dropout**: Mahasiswa putus studi
    - **Enrolled**: Mahasiswa aktif
    - **Graduate**: Mahasiswa lulus
    """
)

# Fitur Utama: Upload Batch CSV Data Mahasiswa
st.write("### 📁 Unggah Data Mahasiswa (.csv)")
st.caption("Pastikan file CSV memiliki kolom fitur mentah yang sesuai dengan format dataset utama.")

uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"])

if uploaded_file is not None:
    # 1. Read Raw CSV Data
    df_raw = pd.read_csv(uploaded_file, sep=";")

    # Hapus kolom 'Status' jika ada di file unggahan (agar tidak ikut ter-scale/prediksi)
    if "Status" in df_raw.columns:
        df_features = df_raw.drop(columns=["Status"])
    else:
        df_features = df_raw.copy()
    
    with st.expander("👁️ Lihat Preview Data Mentah"):
        st.dataframe(df_raw.head(10), use_container_width=True)

    # Inisialisasi session state untuk menyimpan hasil prediksi
    if "df_result" not in st.session_state:
        st.session_state.df_result = None
    if "preds" not in st.session_state:
        st.session_state.preds = None

    if st.button("🚀 Jalankan Prediksi", type="primary"):
        with st.spinner("Memproses preprocessing data & menjalankan prediksi..."):
            # 2. Preprocessing Data (Scaling -> PCA 22)
            df_preprocessed = data_preprocessing(data=df_features)

            # 3. Running Prediction Model
            preds = prediction(data=df_preprocessed)

            # 4. Tambahkan Hasil Prediksi ke DataFrame Utama
            df_result = df_raw.copy()
            df_result["Hasil_Prediksi"] = preds

            # Simpan di session_state
            st.session_state.df_result = df_result
            st.session_state.preds = preds

        # Jika prediksi sudah tersedia di session_state, tampilkan hasilnya
        if st.session_state.df_result is not None:
            st.success("✅ Prediksi Berhasil Diselesaikan!")

            # Ringkasan Hasil Prediksi
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
            st.dataframe(st.session_state.df_result, use_container_width=True)

            # 5. Tombol Unduh & Tombol "Mau prediksi lagi?" Bersisian
            col_btn1, col_btn2, _ = st.columns([1, 1, 2])

            csv_data = st.session_state.df_result.to_csv(index=False).encode("utf-8")

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
                if st.button(
                    "🔄 Mau prediksi lagi?", type="primary", use_container_width=True
                ):
                    # Reset session state dan refresh halaman
                    st.session_state.df_result = None
                    st.session_state.preds = None
                    st.rerun()

else:
    # Reset state jika pengguna menghapus/mengganti file upload
    st.session_state.df_result = None
    st.session_state.preds = None
    st.info(
        "Silakan unggah file CSV data mahasiswa di atas untuk memulai analisis prediksi."
    )