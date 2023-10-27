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
def read_input_file(input_file):
  # To start with, we check if the input file exists and if it is a file.
  if os.path.exists(input_file) and os.path.isfile(input_file):
    extension = os.path.splitext(input_file)[1]
    if extension != ".txt":
      print("The input file must be a `.txt` file.")
      sys.exit(1) # Exit with error type 1.
    else:
      try:
        with open(input_file, 'r') as file: # Open the file in read mode.
          rows = []
          for line in file:
            rows.append(line.strip().split())
          print()
          print("Would you like to see the content of the file? [y/n]")
          answer = input()
          if answer == "y":
            print()
            print("The content of the file is the following:")
            for line in rows:
              print(line)
      except FileNotFoundError:
        print(f"The file {input_file} doesn't exist.")
        sys.exit(1)
      except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        sys.exit(1)
        
      return rows