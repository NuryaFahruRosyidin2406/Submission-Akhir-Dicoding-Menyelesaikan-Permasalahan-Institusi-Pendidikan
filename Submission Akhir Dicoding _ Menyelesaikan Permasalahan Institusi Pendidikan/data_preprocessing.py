import joblib
import pandas as pd

# 1. Load objek preprocessing yang sudah disimpan
scaler = joblib.load("model/scaler.joblib")
pca = joblib.load("model/pca_22.joblib")

def clean_numeric_value(val):
    """Memperbaiki format angka string dengan banyak titik desimal/pemisah ribuan."""
    if isinstance(val, str):
        # Jika string memiliki banyak titik (misal '11.666.666.666.666.600')
        if val.count(".") > 1:
            parts = val.split(".")
            val = "".join(parts[:-1]) + "." + parts[-1]
        # Ganti koma dengan titik jika ada
        val = val.replace(",", ".")
    return val

def data_preprocessing(data):
    """Preprocessing data
    Melakukan preprocessing data mentah mahasiswa (Scaling -> PCA 22 Komponen)

    Args:
        data (Pandas DataFrame): Dataframe berisi fitur mentah mahasiswa

    Returns:
        Pandas DataFrame: Dataframe hasil transformasi PCA 22 komponen
    """
    
    # 1. Pastikan data dalam bentuk copy agar tidak merubah dataframe asli
    df_input = data.copy()

    # 2. Hapus kolom target 'Status' jika ada
    if "Status" in df_input.columns:
        df_input = df_input.drop(columns=["Status"])
        
    # 3. Sisipkan kolom 'index' di paling awal jika belum ada
    if "index" not in df_input.columns:
        df_input.insert(0, "index", range(len(df_input))) 
    
    # 4. Pastikan urutan dan nama kolom sama persis dengan yang diharapkan scaler
    if len(df_input.columns) == len(scaler.feature_names_in_):
        df_input.columns = scaler.feature_names_in_
    else:
        df_input = df_input[scaler.feature_names_in_]

    # 5. Membersihkan format angka string & konversi seluruh kolom ke numerik (float)
    for col in df_input.columns:
        df_input[col] = df_input[col].apply(clean_numeric_value)
        df_input[col] = pd.to_numeric(df_input[col], errors="coerce").fillna(0)

    # 6. Transformasi Scaling (StandardScaler)
    data_scaled = scaler.transform(df_input)

    # 7. Transformasi PCA (22 Komponen)
    data_pca = pca.transform(data_scaled)

    # 8. Kembalikan ke format DataFrame dengan penamaan kolom pc_1 s/d pc_22
    pca_cols = [f"pc_{i+1}" for i in range(data_pca.shape[1])]
    df_preprocessed = pd.DataFrame(data_pca, columns=pca_cols)
    
    return df_preprocessed