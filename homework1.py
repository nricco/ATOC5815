"""
ATOC-5815 homework 1 Due Aug. 30th

Practice python flow control and functions following the
discussions at https://www.pythoncheatsheet.org/
"""

def fuelConsumption(a_fuel0, a_speed, a_trip):
    '''
        Calculate the distance traveled and fuel level for a vehicle
        traveling at a constant speed. 
        
        arguments: a_fuel0 = initial fuel (volume)
                   a_speed = speed (distance/time)
                   a_trip = trip planned (distance)
        results: fuel_level = leftover fuel 
                 dist = distance traveled 
    '''
    fuel_level = a_fuel0 
    t = 0.0
    dist = 0.0
    
    while fuel_level >= 0.0:
        dist = dist + a_speed * t  
        fuel_level = fuel_level - (0.05 * a_speed + 0.00025 * a_speed **2)
        if dist > a_trip:
            break
            
        t = t + 0.5
        
    return fuel_level, dist

def tripStatus(a_trip, a_dist, a_fuel):
    if (a_dist > a_trip): 
        print("You made it!! with %.1f gallons left" % a_fuel)
    else:
        print("You did NOT make it...\n You still have %1.0f miles to go" \
                  % (a_trip-a_dist))

# Test out the functions with two different trips (fuel, speed, distance)
tripA = 200.0
print("Trip A: {} miles".format(tripA))
fuelA, travelA = fuelConsumption(20.0, 40.0, tripA)
tripStatus(tripA, travelA, fuelA)

tripB = 200.0
print("Trip B: {} miles".format(tripB))
fuelB, travelB = fuelConsumption(10.0, 50.0, tripB)
tripStatus(tripB, travelB, fuelB)
    

