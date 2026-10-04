import pandas as pd

def transform_data(df):
    # Example transformation: drop rows with missing values
    before = len(df)
    df= df.drop_duplicates() 
    duplicates_removed = before - len(df)
    print(f"Filas duplicadas eliminadas: {duplicates_removed}")

    for column in df.select_dtypes(include=['object']).columns:
        df[column] =  df[column].astype("category")

        print("Transformacion completada")
        return df
    