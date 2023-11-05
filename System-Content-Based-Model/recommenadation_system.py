##
# File name: recommendation_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 27/10/2023
# Description: .
# This is the documentation of the recommendation system based on the content based model project implemented by Samuel Martín Morales and Aday Chocho Aisa.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import os
import sys
import numpy as np
import string

# FILE IMPORTS
from read_input_files import read_input_files
from read_input_files import read_input_lines_files
from read_input_files import read_lematization_of_terms_file
from write_file_system import write_file_system

##
  # @brief Implements the function that calculates the final table that contains different relevant metrics.
  #
  # @param document_file the input file that contains the different documents.
  # @param stop_word_file the input file that contains the different stop words.
  # @param lematization_of_terms_file the input file that contains the different lematization of terms.
  # @return The final table that contains different relevant metrics.
#
def recommendation_system(document_file, stop_word_file, lematization_of_terms_file):
  print("Welcome to the recommendation system!")
  print()
  print("The introdiced data is the following:")
  print("Input file: " + str(document_file))
  print("Stop Word file: " + str(stop_word_file))
  print("Lematization of terms file " + str(lematization_of_terms_file))
  
  stop_word_data = read_input_lines_files(stop_word_file)
  
  documents = read_input_lines_files(document_file)

  # Deleting punctuation and casefold.
  translator = str.maketrans("", "", string.punctuation)

  for i in range(len(documents)):
    documents[i] = documents[i].translate(translator)
    documents[i] = documents[i].casefold()

  for i in range(len(documents)):
    documents[i] = documents[i].split(" ")

  # Deleting stop words.
  for i in range(len(documents)):
    documents[i] = [word for word in documents[i] if word not in stop_word_data]
        
  lematization_of_terms_data = read_lematization_of_terms_file(lematization_of_terms_file)
  
  # Lematization of terms.
  for i in range(len(documents)):
    for j in range(len(documents[i])):
      for k in range(len(lematization_of_terms_data)):
        if documents[i][j] in lematization_of_terms_data[k][0]:
          documents[i][j] = lematization_of_terms_data[k][1]
          break
          
  documents_matrices = []
  
  for i in range(len(documents)):
    documents_matrices.append([])
    for word in documents[i]:
      if word not in documents_matrices[i]:
        documents_matrices[i].append(word)

  # For each document, we add the index of the word.
  for i in range(len(documents_matrices)):
    for j in range(len(documents_matrices[i])):
        documents_matrices[i][j] = [j, documents_matrices[i][j]]
  
  # Word occurrence counter per document
  for i in range(len(documents_matrices)):
    for j in range(len(documents_matrices[i])):
      documents_matrices[i][j].append(documents[i].count(documents_matrices[i][j][1]))
      
  # DF and IDF calculation
  for i in range(len(documents_matrices)):
    for j in range(len(documents_matrices[i])):
      documents_matrices[i][j].append(0) # DF
      for k in range(len(documents_matrices)):
        if documents_matrices[i][j][1] in documents[k]:
          documents_matrices[i][j][3] += 1  
      documents_matrices[i][j].append(np.log10(len(documents)/documents_matrices[i][j][3]))

  # TF calculation
  for i in range(len(documents_matrices)):
    for j in range(len(documents_matrices[i])):
      documents_matrices[i][j].append(1 + np.log10(documents_matrices[i][j][2]))  # TF

  # TF-IDF calculation
  for i in range(len(documents_matrices)):
    lenght_of_vector = 0
    for j in range(len(documents_matrices[i])):
      lenght_of_vector += documents_matrices[i][j][5] ** 2
    lenght_of_vector = np.sqrt(lenght_of_vector)
    for j in range(len(documents_matrices[i])):
      documents_matrices[i][j].append(lenght_of_vector)
      documents_matrices[i][j].append(documents_matrices[i][j][5] / lenght_of_vector)

  # Similarity calculation
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
        for k in range(len(documents_matrices[j])):
          if documents_matrices[j][k][1] == word_values[0]:
            word_values.append(documents_matrices[j][k][7])
            break
      if j == len(documents)-1:
        word_similarity[i] = word_values

  sim_matrix = []
  for i in range(len(documents)):
    sim_matrix.append([])
    for j in range(len(documents)):
      sim_matrix[i].append(0.0)
      for k in range(len(word_similarity)):
        sim_matrix[i][j] += word_similarity[k][i+1]*word_similarity[k][j+1]
  
  write_file_system(documents_matrices, document_file, sim_matrix)