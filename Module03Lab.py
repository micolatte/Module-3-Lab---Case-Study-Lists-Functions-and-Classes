class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__(vehicle_type="car")  
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
def main():
    print("Welcome to the Automobile Information App!")
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    while True:
        doors = input("Enter the number of doors (2 or 4): ")
        if doors in ['2', '4']:
            break
        else:
            print("Invalid input. Please enter either 2 or 4.")
    while True:
        roof = input("Enter the type of roof (solid or sun roof): ").lower()
        if roof in ['solid', 'sun roof']:
            break
        else:
            print("Invalid input. Please enter either 'solid' or 'sun roof'.")
    car = Automobile(year, make, model, doors, roof)
    print("\nHere is the information you entered:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")
if __name__ == "__main__":
    main()
