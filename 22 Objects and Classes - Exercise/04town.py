class Town:
    def __init__(self, name: str, latitude="0°N", longitude="0°E"):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


# Part below is test code from example


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

#################################### TASK CONDITION ############################
'''
                       4.	Town
Create a class Town. The __init__ method should receive the name of 
the town (string). Each town has a latitude - "0°N" upon initialization 
and a longitude - "0°E" upon initialization. It should also have 3 more methods:
•	set_latitude(latitude) - sets an latitude
•	set_longitude(longitude) - sets an longitude
•	__repr__ - returns a representation of the object in the following string format:
"Town: {name} | Latitude: {latitude} | Longitude: {longitude}"

_______________________________________________
Example

Test Code	(no input data in this task)

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

Output
Town: Sofia | Latitude: 42° 41' 51.04" N | Longitude: 23° 19' 26.94" E

'''
