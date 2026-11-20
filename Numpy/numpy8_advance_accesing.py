import numpy as np
#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
print(car_hp_arr)
print(car_hp_arr[0])
print(car_hp_arr[1])
print(car_hp_arr[0][0])
print(car_hp_arr[0][-1])