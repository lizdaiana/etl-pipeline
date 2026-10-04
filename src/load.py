def load_data(df, out_path):

    df.to_parquet(out_path, index=False)

    print(f"datos exportados exitosamenente a : {out_path}")


