import pandas as pd


def extract_data(file_path):
    df = pd.read_csv(file_path)
    print(f"dataset cargado: {len(df)} filas, {len(df.columns)} columnas")
    return df
