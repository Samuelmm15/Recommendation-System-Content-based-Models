# File name: write_file_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that write the results of the program into a output file.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import os
import numpy as np
import sys

from prettytable import PrettyTable

##
  # @brief Implements the function that write the results of the program into a output file.
  #
  # @param prediction_matrix the prediction matrix.
  # @param similarity_matrix the similarity matrix.
  # @param prediction_history the prediction history.
  # @param metrics the metrics that the user wants to use to calculate the similarity between users.
  # @param number_of_neighbours the number of neighbours that the user wants to use to calculate the prediction.
  # @param type_of_prediction the type of prediction that the user wants to use to calculate the prediction.
  # @param file_name the name of the input file.
#
def write_file_system(document_matrix,  document_file, sim_matrix):
  # Al hacer uso de distintos tipos de ficheros de entrada, se obtienen distintos ficheros de salida.
  for i in range(len(document_matrix)):
    path = document_file
    file_name =  os.path.basename(path) # Allows to obtain the file name, removing the path.
    file_name = os.path.splitext(file_name)[0] # Allows to obtain the file name, removing the extension.
    output_file_name = f"../Results/{str(file_name)}_{str(i)}_output.txt"

    with open(output_file_name, "w") as file:
      file.write("<< TABLE >>\n\n")

    # Creación de la tabla para mostrar los resultados y posteriormente se realiza su impresión en un documento externo.
    table = PrettyTable()
    table.field_names = ["Index", "Word", "Frequency", "TF", "DF", "IDF", "Length of vector"]
    
    output_document_matrix = document_matrix[i]
    for i in output_document_matrix:
      table.add_row([str(i[0])[:10], str(i[1])[:10], str(i[2])[:10], str(i[3])[:10], str(i[4])[:10], str(i[5])[:10], str(i[6])[:10]]) # Haciendo uso del :10 permite establecer el número máximo de caracteres por columna.
    
    # Ajuste del estilo y el ancho del relleno de la tabla
    # Establecer estilo de alineación para los encabezados
    # for field in table.field_names:
    #     table.padding_width = 10
    table.padding_width = 10
    
    # Centrado del contenido de cada columna
    table.align["Index"] = "c"
    table.align["Word"] = "c"
    table.align["Frequency"] = "c"
    table.align["TF"] = "c"
    table.align["DF"] = "c"
    table.align["IDF"] = "c"
    table.align["Length of vector"] = "c"

    sim_text = ""
    print(sim_matrix)
    for j in range(len(sim_matrix[i])):
      if i != j:
        sim_text += "Similaridad entre documento " + str(i) +" y documento " + str(j) + " = " + str(sim_matrix[i][j]) + "\n"


    # Impresión de la tabla en el documento externo.
    with open(output_file_name, "a") as file:
      file.write(str(table))
      file.write("\n\n")
      file.write(sim_text)
      file.write("\n\n")
  sys.exit(0) # Exit with success.