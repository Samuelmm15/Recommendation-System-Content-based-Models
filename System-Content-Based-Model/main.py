##
# File name: main.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 27/10/2023
# Description: Main file of the project.
# @mainpage Recommendation System
# @section intro_sec Introduction
# This is the documentation of the recommendation system based on the content based model project implemented by Samuel Martín Morales and Aday Chocho Aisa.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import os
import sys
import click

# FILE IMPORTS
from recommenadation_system import recommendation_system

##
  # @brief Implements the help menu of the program.
  #
  # @return The help menu if the user needs it.
def help_menu():
  print("Welcome to the support menu!")
  print()
  print("To use the recommendation system, you must to use the following structure:")
  print()
  print("# python3 main.py -i <inputfile> -p <stop-word-file> -l <lematization-of-terms-file>")
  print()
  print("Where:")
  print("<inputfile> is the path to the input file that contains the utility matrix.")
  print("<stop-word-file> is the path to the file that contains the stop words.")
  print("<lematization-of-terms-file> is the path to the file that contains the lematization of terms.")
  sys.exit(0) # Exit with success.

# Implementation of the command-line arguments.
@click.command()
@click.option('-t', help='Path to the input file that contains the plain text file.')
@click.option('-p', help='Path to the file that contains the stop words.')
@click.option('-l', help='Path to the file that contains the lematization of terms.')
@click.option('-h', help='Show the help menu.', is_flag=True)
def main(t, p, l, h):  # Main function of the program
  if h:
    help_menu()
  elif t and p and l:
    if not os.path.isfile(t):
      print("The text input file doesn't exist.")
      help_menu()
      sys.exit(1) # Exit with error type 1.
    if not os.path.isfile(p):
      print("The stop words input file doesn't exist.")
      help_menu()
      sys.exit(1) # Exit with error type 1.
    if not os.path.isfile(l):
      print("The lemmatization input file doesn't exist.")
      help_menu()
      sys.exit(1) # Exit with error type 1.
    else:
      recommendation_system(t, p, l)
  else:
    print("Error: You must to introduce the three files.")
    help_menu()
    sys.exit(1) # Exit with error type 1.
  sys.exit(0) # Exit with success.

if __name__ == "__main__":
  main() # Call to the main function of the program.