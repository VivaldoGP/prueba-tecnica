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

def nullData(inFile):
    data = pd.read_csv(inFile)
    columns = data.columns.values.tolist()

    nullDict = {}
    for col in columns:
        nullDict[col] = data[col].isna().sum()
        

    return nullDict
    

def getConnection():
    
    dialect = getenv('DIALECT')
    username = getenv('USERNAME')
    password = getenv('PASSWORD')
    host = getenv('HOST')
    port = getenv('PORT')
    database = getenv('DATABASE')

    conn = create_engine(f"{dialect}://{username}:{password}@{host}:{port}/{database}")

    return conn

def exportDataToDB(inFile: str, naColumns: list, expColumns: list, con):

    df = pd.read_csv(inFile)
    df = df.dropna(subset=naColumns)

    return print(df[expColumns].shape)
    


#nullData("../Seccion1/results/data_prueba_tecnica_cleaned.csv")


#exportDataToDB(inFile="../Seccion1/results/data_prueba_tecnica_cleaned.csv", naColumns=["id"], expColumns=["id", "name", "company_id"])

getConnection()