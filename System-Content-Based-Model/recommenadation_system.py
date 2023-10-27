##
# File name: recommendation_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 27/10/2023
# Description: .
# This is the documentation of the recommendation system based on the content based model project implemented by Samuel Martín Morales and Aday Chocho Aisa.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

import os
import sys
import numpy as np

from read_input_files import read_input_files
from read_input_files import read_input_lines_files

def recommendation_system(plain_text_file, stop_word_file, lematization_of_terms_file):
  print("Welcome to the recommendation system!")
  print()
  print("The introdiced data is the following:")
  print("Input file: " + str(plain_text_file))
  print("Stop Word file: " + str(stop_word_file))
  print("Lematization of terms file " + str(lematization_of_terms_file))
  
  # Lectura de las palabras de parada
  stop_word_data = read_input_lines_files(stop_word_file)
  
  # Lectura de los ficheros de documentos que se encuentran dentro de el fichero plain_text_file.
  plain_text_data = read_input_lines_files(plain_text_file)
  documents = []
  for line in plain_text_data:
    path = "../Data/Documents/" + line.replace("\n", "")
    documents.append(read_input_files(str(path)))
  
  # lematization_of_terms_data = read_input_file(lematization_of_terms_file)
  
  # At this point starts the implementation of the content based model.
  
  # # First of all, we need to obtain the different terms of the plain text file.
  # terms = []
  # for line in plain_text_data:
  #   for term in line:
  #     if term not in terms:
  #       terms.append(term)
  
  # # Comprobación de que se han obtenido bien los términos.
  # print()
  # print("The different terms of the plain text file are the following:")
  # print(terms)