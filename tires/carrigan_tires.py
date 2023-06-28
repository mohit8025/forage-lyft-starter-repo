from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        count = 0
        for x in self.tire_array:
            if x >= 0.9:
                count += 1
        return count >= 1