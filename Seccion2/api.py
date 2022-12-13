import numpy as np


class FirstNNumbers:

    """
    Esta clase representa el conjunto de los n primeros numeros naturales(comenzando por el 1),\n
    para que su uso no se vea limitado a unicamente los primeros 100, para esto se define el conjunto\n
    como un un array espaciado del 1 a n-1, donde n es el valor máximo que el usuario\n
    desee.
    Los métodos de la clase son los siguientes:
    """
    def __init__(self, nums: int):
        """
        Constructor de la clase.

        Args:
            nums (int): Al crear una instancia de la clase se define la longitud del conjunto,\n
                        esta longitud sirve como párametro para crear el array sobre el cual\n
                        se tienen los numeros pertenecientes al conjunto.
        
        Attributes:
            setOfNumbers: El array con el conjunto de los n numeros.
            totalSum:La suma de todos los elementos en el conjunto.
            toExtract: Valor introducido por el usuario para extraerlo del conjunto.
            numberExtracted: Elemento extraido del conjunto, calculado a partir de la resta\n
                            con la suma del conjunto.
        """        
        self.nums = nums
        self.setOfNumbers = np.arange(1, self.nums + 1)
        self.totalSum = self.sumOfSet()
        self.toExtract = self.extractNumber()
        self.numberExtracted = self.totalSum - self.extractDiff()
    


    def sumOfSet(self):
        """
        Realiza la suma de todos los elementos en el conjunto(array).

        Returns:
            int: Suma de todos los elementos en el conjunto.
        """        
        total = np.sum(self.setOfNumbers)
        return total

    def extractNumber(self):
        """
        Se le pide al usuario que introduzca el numero que desea extraer\n
        del conjunto. Se añade la validación del input de forma que si\n
        se introduce un tipo de dato no válido la solicitud continua y\n
        hasta que el input sea válido.

        Returns:
            int: Numero que el usuario desea extraer.
        """        
        while True:
            numToExtract = input("¿Qué numero deseas extraer?: ")
            try:
                numToExtract = int(numToExtract)
            except:
                print("Tipo de dato invalido, ingresa un int.")
                continue
            
            if numToExtract >= self.nums:
                print("El numero está fuera del rango")
                continue
            break

        return numToExtract

    def extractDiff(self):
        """
        Se realiza la resta aritmetica de la suma del conjunto completo\n
        con el valor a extraer. Para después operarse y obtener el numero\n
        que fue extraido.

        Returns:
            int: Diferencia entre la suma del conjunto y el valor a extraer.
        """        
        extracted = self.toExtract
        
        return self.totalSum - extracted

  

#Creacion de una instancia
a = FirstNNumbers(nums=100)
#Suma del conjunto
print(a.sumOfSet())
#Resta entre la suma del conjunto y el numero extraido
print(a.extractDiff())
#Numero a extraer
print(a.toExtract)
#Numero extraido (calculado)
print(a.numberExtracted)