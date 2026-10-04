# ETL Pipeline de Datos

## Descripción
Este proyecto implementa un pipeline ETL (Extract, Transform, Load)
utilizando Python y Pandas para procesar datos desde un archivo CSV.

El pipeline permite extraer datos, limpiarlos y transformarlos,
y exportar el resultado en formato Parquet.

## Tecnologías utilizadas
-visual studio code
- git hub 
- Pandas
- PyArrow
 

## Estructura del proyecto

    etl-pipeline/
    ├── main.py
    ├── src/
    │   ├── _inint_.py
    │   ├── extract.py
    │   ├── transform.py
    │   └── load.py
    ├── data
    ├── requirements.txt
    ├── README.md
    └── pyvenv.md

## Instalación

Clonar el repositorio:

    git clone https://github.com/lizdaiana/etl-pipeline.git

Ingresar a la carpeta:

    cd etl-pipeline

Crear un entorno virtual:

    python -m venv .venv

Activar el entorno virtual en Windows:

    .venv\Scripts\activate

Instalar las dependencias:

    pip install -r requirements.txt

## Dataset de entrada

Colocar el archivo CSV en la carpeta data/.
Se arrastro el arvhibo CSV hasta raw
El nombre y la ruta deben coincidir con los configurados en main.py.



## Ejecución

Desde la carpeta principal, ejecutar:

    python main.py

## Etapas del pipeline

### 1. Extracción
Lee los datos desde un archivo CSV utilizando Pandas.

### 2. Transformación
Normaliza los nombres de las columnas, elimina duplicados,
gestiona valores nulos y optimiza tipos de datos cuando corresponde.

### 3. Carga
Exporta los datos procesados en formato Parquet.

## Justificación del formato Parquet

Parquet es un formato columnar que ofrece compresión eficiente
y permite leer solamente las columnas necesarias. Esto resulta útil
para el análisis de datos y la preparación de conjuntos de datos
para Machine Learning.

## Autor
Liz Gaona
