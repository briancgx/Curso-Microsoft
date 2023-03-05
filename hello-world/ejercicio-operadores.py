# Now you will test both the object's size and proximity. 
# You will use the same threshold for size of 5m3. 
# If the object is both larger than the threshold and within 1000km of the ship evasive maneuvers will be required.

object_size = 10
proximity = 9000

if object_size >= 5 and proximity > 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')