# File name: write_file_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that write the results of the program into a output file.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import os
import numpy as np
import sys

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
def write_file_system(prediction_matrix, similarity_matrix, prediction_history, metrics, number_of_neighbours, type_of_prediction, file_name):
  file_name = os.path.basename(file_name) # Allows to obtain the file name, removing the path.
  file_name = os.path.splitext(file_name)[0] # Allows to obtain the file name, removing the extension.
  output_file_name = f"../results/{str(metrics)}_{str(number_of_neighbours)}_{str(type_of_prediction)}_{str(file_name)}_output.txt"
  
  with open(output_file_name, "w") as file:
    file.write("<< Prediction Matrix >>\n\n")
  
  with open(output_file_name, "a") as file:
    np.savetxt(file, prediction_matrix, fmt='%-10.4f', delimiter="\t")

  with open(output_file_name, "a") as file:
    file.write("\n\n<< User Similarity Matrix >>\n\n")
  
  with open(output_file_name, "a") as file:
    np.savetxt(file, similarity_matrix, fmt='%-10.4f', delimiter="\t")

  with open(output_file_name, "a") as file:
    file.write("\n\n<< Prediction History >>\n\n")

  with open(output_file_name, "a") as file:
    file.write(prediction_history)
  sys.exit(0) # Exit with success.