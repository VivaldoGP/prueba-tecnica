from csv import reader, writer
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv

load_dotenv()


def prepareData(inFile: str, outFile: str):
    """
    Esta función toma como argumento un archivo de preferencia CSV
    y devuelve el mismo archivo sin renglones vacíos.

    Args:
        inFile (str): Ruta del archivo a procesar.
        outFile (str): Ruta del archivo procesado.
    """    

    try:
        with open(inFile, mode="r") as rawFile:
            csvReader = reader(rawFile, delimiter=',')

            with open(outFile, mode="w", newline='') as preparedFile:
                csvWriter = writer(preparedFile, delimiter=',')
                for row in csvReader:
                    if len(row) > 0:
                        csvWriter.writerow(row)
    except FileNotFoundError as e:
        print(f"La ruta no pudo ser encontrada\n"f"{e}")

    else:

        return print("Se ha modificado tu archivo")

#prepareData("../Dataset/data_prueba_tecnica.csv", "../Seccion1/results/data_prueba_tecnica_cleaned.csv")

def nullData(inFile: str):
    """
    Esta pequeña función devuelve la cantidad de renglones nullos\n
    que tiene cada columna en el archivo de entrada.\n
    Tiene como finalidad servir de ayuda visual de como se encuentra\n
    la información de una manera simple y desde la consola.

    Args:
        inFile (str): Ruta del archivo a leer

    Returns:
        Un diccionario con las columnas como las keys y la suma de los\n
        renglones con valores nullos como los values.
    """    
    data = pd.read_csv(inFile)
    columns = data.columns.values.tolist()

    nullDict = {}
    for col in columns:
        nullDict[col] = data[col].isna().sum()
        

    return nullDict
    

def getConnection():
    """

    Establece una conexión con una base de  datos mediante\n
    el objeto create_engine del modulo SQLAchemy, toma los\n
    párametros de conexión desde un archivo de variables de\n
    entorno.


    Returns:
        Un objeto de conexión con SQLAchemy.
    """    
    
    dialect = getenv('DIALECT')
    username = getenv('USERNAME')
    password = getenv('PASSWORD')
    host = getenv('HOST')
    port = getenv('PORT')
    database = getenv('DATABASE')

    conn = create_engine(f"{dialect}://{username}:{password}@{host}:{port}/{database}")

    return conn


def extractData(inFile: str, outFile: str, columnsToExport: list, delimiter: str =','):
    """ Exporta un archivo csv con las columnas deseadas, cumliendo con la condicion\n
    que sus renglones (rows) son tuplas únicas y no nullas.

    Args:
        inFile (str): Ruta del archivo de entrada
        outFile (str): Ruta del archivo de salida
        columnsToExport (list): Lista de columnas para filtrar los datos
        delimiter (str, optional): Delimitador. Defaults to ','.

    Returns:
        Un archivo csv con los datos deseados.
    """        

    df = pd.read_csv(inFile, delimiter)
    print(df[columnsToExport].drop_duplicates().dropna(),"\nSe han exportado tus datos")


    return (df[columnsToExport].drop_duplicates().dropna()).to_csv(outFile, index=False)


def extractDataByUniques(inFile: str, outFile: str, columnsToExport: list, delimiter: str = ","):
    """Crea un subset de los datos a partir de una columna cuyos valores son únicos y sirven\n
    como llaves para relacionar otras columnas, el subset son los renglones pertenecientes las\n
    columnas de entrada y se asegura su unicidad y que no sean nullos.

    Args:
        inFile (str): Ruta del archivo de entrada
        outFile (str): Ruta del archivo de salida
        columnsToExport (list): Lista de columnas que filtraran los datos
        delimiter (str, optional): Delimitador. Defaults to ",".

    Returns:
        Un archivo csv con los valores deseados.
    """


    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    
    df = pd.read_csv(inFile, delimiter=delimiter)
    dfWOduplicates = df.drop_duplicates(subset=["id"])
    dfWOnans = dfWOduplicates.dropna(subset="id")
    dfPrepared = dfWOnans[columnsToExport]
    print(dfPrepared.shape)

    return dfPrepared.to_csv(outFile, index=False)

#extractData(inFile="../Seccion1/results/data_prueba_tecnica_cleaned.csv", outFile="../Seccion1/results/data_prueba_tecnica_companies.csv", columnsToExport=["company_id", "name"])

def exportDataToDB(inFile: str, destinyTable:str, naColumns: list, expColumns: list):
    """Esta función tiene objetivos futuros para trabajar con pandas y SQLAchemy, permite\n
    escribir datos de un DataFrame a una tabla en una base de datos, tomando el objeto de\n
    conexión creado anteriormente para realizar la conexión y poder realizar las transacciones.

    Args:
        inFile (str): Ruta del archivo de entrada
        destinyTable (str): Tabla de la base de datos
        naColumns (list): Columnas con datos nullos
        expColumns (list): Columnas que se desean exportar

    Returns:
        Una transacción con una tabla en una base de datos.
    """
    conn = getConnection()

    df = pd.read_csv(inFile)
    df = df.dropna(subset=naColumns)

    return df[expColumns].to_sql(name=destinyTable, con=conn, index=False)
    #return print(df[expColumns].shape)
    


#nullData("../Seccion1/results/data_prueba_tecnica_cleaned.csv")


#exportDataToDB(inFile="../Seccion1/results/data_prueba_tecnica_cleaned.csv", naColumns=["id"], expColumns=["id", "name", "company_id"])

#extractDataByUniques("../Seccion1/results/data_prueba_tecnica_cleaned.csv", "../Seccion1/results/data_prueba_tecnica_charges_company.csv", ["id", "company_id", "name"])