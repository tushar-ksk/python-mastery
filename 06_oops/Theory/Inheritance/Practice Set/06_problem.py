class Vector:
    def __init__(self, i=0, j=0, k=0):
        self.i = i
        self.j = j
        self.k = k

    def __len__(self):
        if self.i == 0 and self.j == 0 and self.k == 0:
            D = "null"
            print(f"The given vector is {D} vector")
            return 0  # Ensure this returns an integer

        elif (self.i == 0 and self.j == 0) or (self.i == 0 and self.k == 0) or (self.j == 0 and self.k == 0):
            D = "1D"
            print(f"The given vector is {D} vector")
            return 1  # Ensure this returns an integer

        elif self.i == 0 or self.j == 0 or self.k == 0:
            D = "2D"
            print(f"The given vector is {D} vector")
            return 2  # Ensure this returns an integer

        else:
            D = "3D"
            print(f"The given vector is {D} vector")
            return 3  # Ensure this returns an integer

# Example usage:
v1 = Vector(2, 3, 4)
v2 = Vector(1, -2, 0)

len(v1)  # It will print the type and and ignore return
print(len(v2))  # It will print the type and return an integer
