# Write a Python script to store a list of city names in a file ‘cities.txt’

with open('cities.txt', 'w') as f:
    cities = ['Delhi','Mumbai','Kolkata','Bangalore','Chennai','Hyderabad','Pune','Ahmedabad',
              'Surat','Lucknow','Jaipur','Cawnpore']
    for city in cities:
        f.write(city + '\n')