#Your first program

#You will use a Jupyter notebook to create your first program. 
# Your senior officer wants you to create code to perform a couple of utilities. 
# You will start by displaying today's date. 
# Then you will add code to convert parsecs to lightyears.

#This exercise is broken into a series of steps. 
# For each step you will be presented with the goal for the step, followed by an empty cell. 
# Enter your Python into the cell and run it. 
# The solution for each step will follow each cell.
from datetime import date
print(date.today())

parsecs = 11
lightyears = parsecs*3.26
print(str(parsecs)+ " parsecs is "+ str(lightyears)+ " lightyears ")