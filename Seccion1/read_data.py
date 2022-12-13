from csv import reader, writer

def prepareData(inFilename: str, outFilename: str):
    """
    Esta función toma como argumento un archivo de preferencia CSV
    y devuelve el mismo archivo sin renglones vacíos.

    Args:
        filename (str): Ruta del archivo a procesar.
        outFilename (str): Ruta del archivo procesado.
    """    

    try:
        with open(inFilename, mode="r") as rawFile:
            csvReader = reader(rawFile, delimiter=',')

            with open(outFilename, mode="w", newline='') as preparedFile:
                csvWriter = writer(preparedFile, delimiter=',')
                for row in csvReader:
                    if len(row) > 0:
                        csvWriter.writerow(row)
    except FileNotFoundError as e:
        print(f"La ruta no pudo ser encontrada\n"f"{e}")

    else:

        return print("Se ha limpieado tu archivo")

prepareData("../Dataset/data_prueba_tecnica.csv", "../Seccion1/results/data_prueba_tecnica_cleaned.csv")
