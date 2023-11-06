# File name: read_input_file_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that obtains the different lines of the input file.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import os
import sys

##
  # @brief Implements the function that obtains the different lines of the input file.
  #
  # @param input_file the input file.
  # @return The different lines of the input file.
# 
def read_input_lines_files(input_file):
  # To start with, we check if the input file exists and if it is a file.
  if os.path.exists(input_file) and os.path.isfile(input_file):
    extension = os.path.splitext(input_file)[1]
    if extension != ".txt":
      print("The input file must be a `.txt` file.")
      sys.exit(1) # Exit with error type 1.
    else:
      try:
        with open(input_file, 'r', encoding='utf-8-sig') as file: # Open the file in read mode.
          rows = []
          for line in file:
            rows.append(line.replace("\n", ""))
      except FileNotFoundError:
        print(f"The file {input_file} doesn't exist.")
        sys.exit(1)
      except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        sys.exit(1)
        
      return rows

##
  # @brief Implements the function that obtains the different lines of the input file.
  #
  # @param input_file the input file.
  # @return The different lines of the input file.
#
def read_input_files(input_file):
  # To start with, we check if the input file exists and if it is a file.
  if os.path.exists(input_file) and os.path.isfile(input_file):
    extension = os.path.splitext(input_file)[1]
    if extension != ".txt":
      print("The input file must be a `.txt` file.")
      sys.exit(1) # Exit with error type 1.
    else:
      try:
        with open(input_file, 'r', encoding='utf-8-sig') as file: # Open the file in read mode.
          string = ""
          for line in file:
            string += line.replace("\n", "")
      except FileNotFoundError:
        print(f"The file {input_file} doesn't exist.")
        sys.exit(1)
      except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        sys.exit(1)
        
      return string
    
def read_lematization_of_terms_file(input_file):
  # To start with, we check if the input file exists and if it is a file.
  if os.path.exists(input_file) and os.path.isfile(input_file):
    extension = os.path.splitext(input_file)[1]
    if extension != ".txt":
      print("The input file must be a `.txt` file.")
      sys.exit(1)
    else:
      try:
        with open(input_file, 'r', encoding='utf-8-sig') as file: # Open the file in read mode.
          string = ""
          for line in file:
            string += line.replace("\n", "")
          string = string.replace("{", "")
          string = string.replace("}", "")
          lematization_pairs = string.split(",")
          lematization_list = [[],[]]
          for i in range(len(lematization_pairs)):
            lematization_pairs[i] = lematization_pairs[i].replace("\"", "")
            pair = lematization_pairs[i].split(":")
            lematization_list[0].append(pair[0])
            lematization_list[1].append(pair[1])

      except FileNotFoundError:
        print(f"The file {input_file} doesn't exist.")
        sys.exit(1)
      except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        sys.exit(1)
    return lematization_list