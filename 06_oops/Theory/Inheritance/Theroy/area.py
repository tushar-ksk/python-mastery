a = 5
area = a*a
print(area)

class sqr:

    def __init__(self):
        self._side = 0  # Private variable to store side
        self._area = 0  # Private variable to store area

    @property
    def side(self):
        return self._side  # Return the side value
    
    @side.setter
    def side(self, value):
        self._side = value  # Set the side value
        self._area = value * value  # Calculate and store the area

    @property
    def area(self):
        return self._area  # Return the stored area value

s = sqr()
s.side = 5  # Set the side
print(s.area)  # Get the area, which will be 25
