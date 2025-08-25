#Class và Object (Lớp và đối tượng)

class Car():
    def __init__(self, ParameterName, ParameterBrand, ParameteColor):
        self.name = ParameterName
        self.brand = ParameterBrand
        self.color = ParameteColor

    def Drive(self):
        print(f"Bạn đang lái chiếc xe {self.name} màu {self.color}, của hãng xe {self.brand} ")


BMW = Car("BMW", "330i M Sport", "White")
BMW.Drive()





