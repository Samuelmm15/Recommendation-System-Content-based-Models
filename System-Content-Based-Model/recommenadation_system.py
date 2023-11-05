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
import string

from read_input_files import read_input_files
from read_input_files import read_input_lines_files
from read_input_files import read_lematization_of_terms_file
from write_file_system import write_file_system

def recommendation_system(document_file, stop_word_file, lematization_of_terms_file):
  print("Welcome to the recommendation system!")
  print()
  print("The introdiced data is the following:")
  print("Input file: " + str(document_file))
  print("Stop Word file: " + str(stop_word_file))
  print("Lematization of terms file " + str(lematization_of_terms_file))
  
  # Lectura de las palabras de parada
  stop_word_data = read_input_lines_files(stop_word_file)
  
  # Lectura de los ficheros de documentos que se encuentran dentro de el fichero document_file.
  documents = read_input_lines_files(document_file)
  number_of_documents = len(document_file)

  # Eliminación de la puntuación y mayusculas.
  translator = str.maketrans("", "", string.punctuation)

  for i in range(len(documents)):
    documents[i] = documents[i].translate(translator)
    documents[i] = documents[i].casefold()
  
  # Creación de una matriz de palabras (vector por documento).
  for i in range(len(documents)):
    documents[i] = documents[i].split(" ")

  # Eliminación de las palabras de parada.
  for i in range(len(documents)):
    documents[i] = [word for word in documents[i] if word not in stop_word_data]

  # Comprobación del resultado
  # for i in documents:
  #   print(i)
    
  # Lectura del dichero de lematización.
  lematization_of_terms_data = read_lematization_of_terms_file(lematization_of_terms_file)
  
  # Comprobación del resultado
  # print(lematization_of_terms_data)
  
  # Aplicar el fichero de lematización.
  for i in range(len(documents)):
    for j in range(len(documents[i])):
      for k in range(len(lematization_of_terms_data)):
        if documents[i][j] in lematization_of_terms_data[k][0]:
          documents[i][j] = lematization_of_terms_data[k][1]
          break
  
  # Comprobación del resultado
  # print(documents)
  
  # Creación de la matriz de datos y limpieza de palabras repetidas.
  # Nótese que debe de existir una matriz por documento, es decir, un vector de matrices (matrices tridimensionales).
  
  documents_matrix = []
  
  for i in range(len(documents)):
    documents_matrix.append([])
    for word in documents[i]:
      if word not in documents_matrix[i]:
        documents_matrix[i].append(word)

  # Formato de las matrices (Indice - Palabra)
  for i in range(len(documents_matrix)):
    for j in range(len(documents_matrix[i])):
        documents_matrix[i][j] = [j, documents_matrix[i][j]]
      
  # Comprobación del resultado
  # print(documents)
  
  # Contador de aparición de la palabra por documento
  for i in range(len(documents_matrix)):
    for j in range(len(documents_matrix[i])):
      documents_matrix[i][j].append(documents[i].count(documents_matrix[i][j][1]))
      
  # Comprobación del resultado
  # print(documents_matrix)
      
  # Cálculo de DF y IDF
  for i in range(len(documents_matrix)):
    for j in range(len(documents_matrix[i])):
      documents_matrix[i][j].append(0) # DF
      for k in range(len(documents_matrix)):
        if documents_matrix[i][j][1] in documents[k]:
          documents_matrix[i][j][3] += 1  
      documents_matrix[i][j].append(np.log10(len(documents)/documents_matrix[i][j][3]))

  # Cálculo de TF
  for i in range(len(documents_matrix)):
    for j in range(len(documents_matrix[i])):
      documents_matrix[i][j].append(1 + np.log10(documents_matrix[i][j][2])) #TF

  # Cálculo de la longitud del vector (TF-IDF)
  for i in range(len(documents_matrix)):
    lenght_of_vector = 0
    for j in range(len(documents_matrix[i])):
      lenght_of_vector += documents_matrix[i][j][5] ** 2
    lenght_of_vector = np.sqrt(lenght_of_vector)
    for j in range(len(documents_matrix[i])):
      documents_matrix[i][j].append(lenght_of_vector)
      documents_matrix[i][j].append(documents_matrix[i][j][5] / lenght_of_vector)
  
  # Comprobación del resultado: Indice - Palabra - Contador - TF - DF - IDF - Lenght of Vector - TF-IDF
  #print(documents_matrix)

  # Cálculo de la matriz de simiritud
  word_similarity = []
  for i in range(len(documents)):
    for j in range(len(documents[i])):
      if documents[i][j] not in word_similarity:
        word_similarity.append(documents[i][j])

  for i in range(len(word_similarity)):
    word_values = []
    word_values.append(word_similarity[i])
    for j in range(len(documents)):
      if documents[j].count(word_values[0])==0:
        word_values.append(0.0)
      else:
        for k in range(len(documents_matrix[j])):
          if documents_matrix[j][k][1] == word_values[0]:
            word_values.append(documents_matrix[j][k][7])
            break
      if j == len(documents)-1:
        word_similarity[i] = word_values

  # for k in range(len(word_similarity)):
  #   print(word_similarity[k])

  sim_matrix = []
  for i in range(len(documents)):
    sim_matrix.append([])
    for j in range(len(documents)):
      sim_matrix[i].append(0.0)
      for k in range(len(word_similarity)):
        sim_matrix[i][j] += word_similarity[k][i+1]*word_similarity[k][j+1]
  
  write_file_system(documents_matrix, document_file, sim_matrix)