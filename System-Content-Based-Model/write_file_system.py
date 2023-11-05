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
  path = document_file
  file_name =  os.path.basename(path) # Allows to obtain the file name, removing the path.
  file_name = os.path.splitext(file_name)[0] # Allows to obtain the file name, removing the extension.
  output_file_name = f"../Results/{str(file_name)}_output.txt"
  
  # Impresión de la interacción 0
  with open(output_file_name, "w") as file:
      string = "<< TABLE  " + "0" + " >>\n\n"
      file.write(string)
      
  for i in range(len(document_matrix)):
    if i != 0:
      with open(output_file_name, "a") as file:
        string = "<< TABLE  " + str(i) + " >>\n\n"
        file.write(string)

    # Creación de la tabla para mostrar los resultados y posteriormente se realiza su impresión en un documento externo.
    table = PrettyTable()
    table.field_names = ["Index", "Word", "Count", "DF", "IDF", "TF", "Length of vector", "TF-IDF"]
    
    output_document_matrix = document_matrix[i]
    for j in output_document_matrix:
      table.add_row([str(j[0])[:15], str(j[1])[:15], str(j[2])[:15], str(j[3])[:15], str(j[4])[:15], str(j[5])[:15], str(j[6])[:15], str(j[7])[:15]]) # Haciendo uso del :10 permite establecer el número máximo de caracteres por columna.
    
    # Ajuste del estilo y el ancho del relleno de la tabla
    # Establecer estilo de alineación para los encabezados
    # for field in table.field_names:
    #     table.padding_width = 10
    table.padding_width = 5
    
    # Centrado del contenido de cada columna
    table.align["Index"] = "c"
    table.align["Word"] = "c"
    table.align["Count"] = "c"
    table.align["DF"] = "c"
    table.align["IDF"] = "c"
    table.align["TF"] = "c"
    table.align["Length of vector"] = "c"
    table.align["TF-IDF"] = "c"

    sim_text = ""
    for j in range(len(sim_matrix[i])):
        if i != j:
          sim_text += "Similaridad entre documento " + str(i) +" y documento " + str(j) + " = " + str(sim_matrix[i][j]) + "\n"

    # Impresión de la tabla en el documento externo.
    with open(output_file_name, "a") as file:
      file.write(str(table))
      file.write("\n\n")
      file.write(sim_text)
      file.write("\n\n")
  
  print()
  print("The results have been written in the file: " + output_file_name)
  sys.exit(0) # Exit with success.