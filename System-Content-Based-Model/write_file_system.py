# File name: write_file_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that write the results of the program into a output file.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import os
import numpy as np
import sys

# FILE IMPORTS
from prettytable import PrettyTable

##
  # @brief Implements the function that write the results of the program into a output file.
  #
  # @param document_matrix the document matrix.
  # @param document_file the input file that contains the different documents.
  # @param sim_matrix the similarity matrix.
  # @return The results of the program into a output file.
#
def write_file_system(document_matrix,  document_file, sim_matrix):
  path = document_file
  file_name =  os.path.basename(path) # Allows to obtain the file name, removing the path.
  file_name = os.path.splitext(file_name)[0] # Allows to obtain the file name, removing the extension.
  output_file_name = f"../Results/{str(file_name)}_output.txt"
  
  with open(output_file_name, "w") as file:
      string = "<< TABLE  " + "0" + " >>\n\n"
      file.write(string)
      
  for i in range(len(document_matrix)):
    if i != 0:
      with open(output_file_name, "a") as file:
        string = "<< TABLE  " + str(i) + " >>\n\n"
        file.write(string)

    table = PrettyTable()
    table.field_names = ["Index", "Word", "Count", "DF", "IDF", "TF", "Length of vector", "TF-IDF"]
    
    output_document_matrix = document_matrix[i]
    for j in output_document_matrix:
      table.add_row([str(j[0])[:15], str(j[1])[:15], str(j[2])[:15], str(j[3])[:15], str(j[4])[:15], str(j[5])[:15], str(j[6])[:15], str(j[7])[:15]]) # Add a row to the table.
    
    table.padding_width = 5
    
    # Center the table.
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
          sim_text += "Similaridad coseno entre el documento " + str(i) +" y el documento " + str(j) + " = " + str(sim_matrix[i][j]) + "\n"

    with open(output_file_name, "a") as file:
      file.write(str(table))
      file.write("\n\n")
      file.write(sim_text)
      file.write("\n\n")
  
  print()
  print("The results have been written in the file: " + output_file_name)
  sys.exit(0) # Exit with success.