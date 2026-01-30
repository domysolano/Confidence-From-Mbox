# Maestría en Inteligencia Artificial y Analítica de Datos
# Curso: Programación para Analítica Descriptiva y Predictiva
# Semestre: Enero-Junio 2026
# Profesor: Dr. Vicente García Jiménez
# Alumno: Ricardo Solano Monje
# Matrícula: 266221
# Práctica 1: Manejo de Archivos
# Objetivo del programa: Utilizar Python para extraer datos numéricos de archivos utilizando funciones disponibles en la clase string.
# Programa realizado por: Ricardo Solano Monje

# Práctica 1: Manejo de Archivos
"""
En esta practica, se te pide que diseñes un código en Google Colab para analizar el archivo mbox.txt (revisa el laboratorio 1). El código deberá extraer las mediciones contenidas en cada línea que contiene la cadena X-DSPAM-Confidence.

Objetivos:

Tu código debe extraer únicamente los datos numéricos de las líneas que contienen la cadena X-DSPAM-Confidence en el archivo mbox.txt.

Para extraer los datos númericos usa las intrucciones vistas en el laboratorio 1 (startswith).

Aquí no se usan expresiones regulares.

Los datos numéricos los deberás guardar en una lista y posteriormente mostrar los resultados de cada medición encontrada.

Explica brevemente en tu Google Colab qué realiza el código.
"""
"""
*Calcular y mostrar en pantalla:*
* La cantidad de datos extraídos.
* La sumatoria de los datos.
* El promedio de los datos.
* La varianza de los datos.

Observaciones: Este es un ejemplo de línea con su valor confidence:

X-DSPAM-Confidence: 0.8475
"""

#...Los datos numéricos los deberás guardar en una lista...
# Read confidence values from a file and return them as a list of floats.
# Args:  filename (str): Name of the file to read, mbox.txt by default
# Returns: confidence_list (list) : List of confidence values as floats
# Example of line having a confidence value to be extracted: "X-DSPAM-Confidence: 0.8475"
# All string characters are discarded but the numeric one

def read_confidence_values(file_path='mbox.txt'):


    confidence_list = []

    try:
        with open(file_path, 'r') as file:
            all_lines = file.readlines()

        for current_line in all_lines:
            if current_line.startswith('X-DSPAM-Confidence:'): # we must use startswith for finding line "with" X-DSPAM-Confidence...
                colon_index = current_line.find(':') # then find start of colon
                after_colon = current_line[colon_index + 1:] #copy substring after colon
                cleaned = after_colon.strip() # cleans white spaces
                number = float(cleaned) # convert number string to float
                confidence_list.append(number) # adds another float to confidence list

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except ValueError as e:
        print(f"Error converting to float: {e}")
        return []

    return confidence_list

#...posteriormente mostrar los resultados de cada medición encontrada.
# Print all confidence values in the list.
# Args: confidence_list (list): List of confidence values

def print_confidence_values(confidence_list):
    print("-" * 10+"\n")
    print("Extracted Confidence Values:")
    print("-" * 10+"\n")
    for i, number in enumerate(confidence_list, 1):
        print(f"  {i}. {number}")
    print()

#  Wait for user to press Enter.
#  Args: prompt (str): Message to display while waiting

def wait_for_enter(prompt="Press Enter to continue..."):
    print(f"\n{prompt}")
    input()

"""## Variance is calculated using the Population Variance formula:

Population Variance = Σ(xᵢ - μ)² / N

Where:

Σ = Summation (add everything up)

xᵢ = Each individual data point

μ (mu) = Population mean (average)

N = Total number of data points in the population

Mapping to code:

xᵢ == xi

μ (mu) == average

N == num_points

Summation == Σ == squared_diffs_Summation = sum((xi - average) ** 2 for xi in confidence_data)

where sum((xi - average) ** 2 for xi in confidence_data) adds everything up using this special case of "for" loop.

variance== Σ(xᵢ - μ)² / N == squared_diffs_Summation / num_points
"""

# Calcular y mostrar en pantalla: La cantidad de datos extraídos,La sumatoria de los datos,El promedio de los datos,La varianza de los datos.

# function to Calculate and print statistics for the confidence values.
# Args: confidence_list (list): List of confidence values.

def calculate_statistics(confidence_data):

    num_points = len(confidence_data)


    if num_points > 0:
        print(f"1. Number of extracted data points: {num_points}")
        # Calculate sum
        sum_values = sum(confidence_data) #built-in function apply to an iterable list
        print(f"2. Sum of data points: {sum_values}")

        # Calculate average
        average = sum_values / num_points
        print(f"3. Average of data points: {average:.6f}")

        # Calculate variance
        squared_diffs_Summation = sum((xi - average) ** 2 for xi in confidence_data)
        population_variance = squared_diffs_Summation / num_points
        print(f"4. Variance of data points: {population_variance:.6f}")
    else:
      print("No data points to calculate statistics.")
      return

#  Main function for reading, printing, and analysing confidence values

def main():
    # File path
    file_path = "mbox.txt"
    print("-" * 10+"\n")
    print("DSPAM Confidence Analysis")
    print("-" * 10+"\n")
    #Read confidence values from file
    confidence_data = read_confidence_values(file_path)

    #  ...y posteriormente mostrar los resultados de cada medición encontrada.


    # Calculate and print statistics, these go first so as to be able to see them

    calculate_statistics(confidence_data)

    #  Ask user to continue, then show all stored confidence values
    wait_for_enter("\n Press Enter to view ALL extracted confidence values...\n")

    # Print the extracted values
    print_confidence_values(confidence_data)

    print("-" * 10+"\n")
    print("DSPAM Confidence Analysis")
    print("-" * 10+"\n")
    calculate_statistics(confidence_data) #printed twice so as to be seen at the beginning as well as at the end.

# Call the main function
if __name__ == "__main__":
    main()