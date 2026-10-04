from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

#ruta
RUTA_CSV_ORINGEN ="data/raw/dataset.csv"
RUTA_PARQUET_DESTINO = "data/processed/dataset_procesado.parquet"


def main():
    print("Iniciando el proceso ETL")

    # Extract
    print("Etapa 1 : Extranccion de datos")
    df = extract_data(RUTA_CSV_ORINGEN)

    # Transform
    print("Etapa 2 : Transformacion de datos")
    df_transformando = transform_data(df)

    # Carga
    print("Etapa 3 : Carga de datos")
    load_data(df_transformando, RUTA_PARQUET_DESTINO)
    print("\n Pipeline ejecutado con exito")

    if __name__ == "__main__":
        main()

        