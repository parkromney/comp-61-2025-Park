class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"

class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars_owned = []

    def purchase_car(self, car):
        self.cars_owned.append(car)
        print(f"{self.name} just purchased a {car.get_car_info()}.")

    def show_owned_cars(self):
        if not self.cars_owned:
            print(f"{self.name} doesn't own any cars yet.")
        else:
            print(f"{self.name} owns the following cars:")
            for car in self.cars_owned:
                print(f"  - {car.get_car_info()}")


def main():
    owner1 = Owner("Park", 30)
    owner2 = Owner("Ashley", 25)

    car1 = Car("Dodge", "Ram 1500", 2011)
    car2 = Car("Ford", "F-150", 2019)
    car3 = Car("Toyota", "4runner", 2018)
    car4 = Car("Chevrolet", "Malibu", 2018)

    owner1.purchase_car(car1)
    owner1.purchase_car(car2)
    owner2.purchase_car(car3)
    owner2.purchase_car(car4)

    owner1.show_owned_cars()
    owner2.show_owned_cars()

if __name__ == "__main__":
    main()
