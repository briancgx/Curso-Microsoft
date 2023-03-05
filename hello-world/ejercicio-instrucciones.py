#You will start your project by creating the code to determine if a piece of space debris is of a dangerous size. 
# For this exercise we will use an arbitrary size of 5 meters cubed (5m3); anything larger is a potentially dangerous object.

object_size = 10
if object_size >= 5:
    print('We need to keep an eye on this object')
else:
    print('Object poses no threat')