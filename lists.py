#example list:
car_brands = ['Tesla', 'Audi', 'Hona', 'BMW', 'Mercedes']
print(car_brands)

# #accessing certian items in the list 
print(car_brands[1])
# #output = Audi.

print(car_brands[0].title)
#This prints the car brand titled, you can also do ".upper" or ".lower"

car_brands.append('Volkswagen')
print(car_brands)
car_brands.insert(0,"Ferrari")
#This inserts "Ferrari" at the beginning of the list

car_brands.sort()
#Sorting the car brand list

car_brands.sort(reverse=True)
#this sorts the car brand list in reverse. i.e. reverse=False => A-Z, reverse=True => Z-A.

