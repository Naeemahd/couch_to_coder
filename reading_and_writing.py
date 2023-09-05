import csv
from collections import namedtuple

Car = namedtuple( "Car", " model year price transmission mileage fuelType tax mpg engineSize")
cars = []
with open("vw.csv", "r", encoding = "utf-8", errors = 'ignore') as csvfile:
    reader = csv. reader (csvfile, skipinitialspace=True)
    next (reader)
    for row in reader:
        new_car = Car(* row)
        cars. append (new_car)

most_expensive_vw_car = []
current_car = cars[0]

for car in cars:
        if car.price > current_car.price:
            current_car = car
most_expensive_vw_car.append (current_car)

sum_of_vw_golf = 0
num_of_vw_cars = 0

for car in cars:
    if car.model == "Golf":
        sum_of_vw_golf += int (car.price)
        num_of_vw_cars += 1

avg_price = sum_of_vw_golf / num_of_vw_cars
print (f"The average price of VW Golf cars is {avg_price}")

sum_of_Polo_in_2020 = 0
num_of_Polo_in_2020 = 0

for car in cars:
    if car.model == "Polo" and int (car. year) == 2020:
        sum_of_Polo_in_2020 += int (car.mileage)
        num_of_Polo_in_2020 += 1

avg_mileage = sum_of_Polo_in_2020 / num_of_Polo_in_2020
print (f"The average mileage of VW Polo models registered in 2020 is {avg_mileage}")

used_vw_cars =[]
for car in cars:
    vw_cars = Car(
        car.model, 
        car.year,
        car.price,
        car.transmission,
        car.mileage, 
        car.fuelType, 
        car.tax, 
        car.mpg, 
        car.engineSize
    )
    used_vw_cars. append (vw_cars)

print(used_vw_cars)
