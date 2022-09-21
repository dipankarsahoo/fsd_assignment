# Write a Python script to append list of city names in a file ‘cities.txt’

with open('cities.txt', 'a') as f:
    cities = ['Mirzapur','Nagpur','Ghaziabad','Indore',
              'Vadodara','Vishakhapatnam','Bhopal','Chinchvad','Patna','Ludhiana','Agra','Kalyan',
              'Madurai','Jamshedpur','Nasik','Faridabad','Aurangabad','Rajkot','Meerut','Jabalpur']
    for city in cities:
        f.write( '\n' + city)