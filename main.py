"""
Chatbot
Author: Garrett Tiller
Period/Core: 5

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")
  # This asks a question and stores it as x
  x= str(input("How are you today: "))
  if x == "good" or "great" or "amazing":
    print("Thats good to hear!")
  else: 
    print("I'm sorry to hear that.")
  z= str(input("Do you like rollercoasters? "))
  if z == "yes" or "Yes":
    print("Thats great, me too")
  else:
    print("Oh...")
  c= str(input("What is one job/place you would like to do/work at?"))
  r=random.randint(1,3)
  if r==1:
    print("Thats so cool, sounds fun!")
  elif r==2:
    print("I wouldn't mind that either. ")
  elif r==3:
    print("Thats an intresing choice, but thats not my style")
if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()