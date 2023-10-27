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

from read_input_file_system import read_input_file

def recommendation_system(plain_text_file, stop_word_file, lematization_of_terms_file):
  print("Welcome to the recommendation system!")
  print()
  print("The introdiced data is the following:")
  print("Input file: " + str(plain_text_file))
  print("Stop Word file: " + str(stop_word_file))
  print("Lematization of terms file " + str(lematization_of_terms_file))
  
  plain_text_data = read_input_file(plain_text_file)
  stop_word_data = read_input_file(stop_word_file)
  lematization_of_terms_data = read_input_file(lematization_of_terms_file)