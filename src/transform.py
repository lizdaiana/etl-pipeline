import pandas as pd

def transform_data(df):
    # Example transformation: drop rows with missing values
    before = len(df)
    df= df.drop_duplicates() 
    duplicates_removed = before - len(df)
    print(f"Filas duplicadas eliminadas: {duplicates_removed}")

    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(r"[^a-z0-9_]", "", regex=True)
    )

    for column in df.select_dtypes(include=['object']).columns:
        df[column] =  df[column].astype("category")

        print("Transformacion completada")
        return df
    
