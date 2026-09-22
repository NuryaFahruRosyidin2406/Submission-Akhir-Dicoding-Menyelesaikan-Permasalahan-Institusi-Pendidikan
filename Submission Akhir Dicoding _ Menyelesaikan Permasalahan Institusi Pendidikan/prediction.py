import joblib

# 1. Load model terbaik dan label encoder
model = joblib.load("model/log_model.joblib")
label_encoder = joblib.load("model/encoder_status.joblib")

def prediction(data):
    """
    Melakukan prediksi status akademis mahasiswa
    
    Args:
        data (Pandas DataFrame): Dataframe hasil preprocess (PCA 22 komponen)
        
    Returns:
        str / list: Hasil prediksi status mahasiswa (Dropout, Enrolled, atau Graduate)
    """
    # 1. Prediksi angka label menggunakan model Logistic Regression
    result = model.predict(data)
    
    # 2. Decode angka label menjadi teks asli
    final_result = label_encoder.inverse_transform(result)
    
    # Jika input hanya 1 baris data, kembalikan berupa string tunggal
    if len(final_result) == 1:
        return final_result[0]
    
    # Jika input berupa batch/banyak baris, kembalikan dalam bentuk array/list
    return final_result