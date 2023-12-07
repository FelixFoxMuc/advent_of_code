seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

source = ""

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        # skip line if empty
        if line == "":
            continue

        # get seeds
        if "seeds" in line:
            seeds = line.split(" ")[1:]

        # set actions
        elif "seed-to-soil" in line:
            source = "seed-to-soil"
            continue

        elif "soil-to-fertilizer" in line:
            source = "soil-to-fertilizer"
            continue

        elif "fertilizer-to-water" in line:
            source = "fertilizer-to-water"
            continue

        elif "water-to-light" in line:
            source = "water-to-light"
            continue

        elif "light-to-temperature" in line:
            source = "light-to-temperature"
            continue

        elif "temperature-to-humidity" in line:
            source = "temperature-to-humidity"
            continue

        elif "humidity-to-location" in line:
            source = "humidity-to-location"
            continue

        # sort according to action
        if source == "seed-to-soil":
            seed_to_soil.append(line.split(" "))

        elif source == "soil-to-fertilizer":
            soil_to_fertilizer.append(line.split(" "))

        elif source == "fertilizer-to-water":
            fertilizer_to_water.append(line.split(" "))

        elif source == "water-to-light":
            water_to_light.append(line.split(" "))

        elif source == "light-to-temperature":
            light_to_temperature.append(line.split(" "))

        elif source == "temperature-to-humidity":
            temperature_to_humidity.append(line.split(" "))

        elif source == "humidity-to-location":
            humidity_to_location.append(line.split(" "))

# print(seeds)
# print(seed_to_soil)
# print(soil_to_fertilizer)
# print(fertilizer_to_water)
# print(water_to_light)
# print(light_to_temperature)
# print(temperature_to_humidity)
# print(humidity_to_location)

soil_dict = {}
for seed in seeds:
    for direction in seed_to_soil:
        if int(direction[1]) <= int(seed) <= int(direction[1]) + int(direction[2]):
            soil = int(seed) + int(direction[0])-int((direction[1]))
            soil_dict[int(seed)] = soil
            break
for seed in seeds:
    if int(seed) not in soil_dict:
        soil_dict[int(seed)] = int(seed)

print(soil_dict)
soils = list(soil_dict.values())
print(soils)

fertilizer_dict = {}
for soil in soils:
    for direction in soil_to_fertilizer:
        if int(direction[1]) <= int(soil) <= int(direction[1]) + int(direction[2]):
            fertilizer = int(soil) + int(direction[0])-int((direction[1]))
            fertilizer_dict[int(soil)] = fertilizer
            break
for soil in soils:
    if int(soil) not in fertilizer_dict:
        fertilizer_dict[int(soil)] = int(soil)

print(fertilizer_dict)
fertilizers = list(fertilizer_dict.values())
print(fertilizers)

water_dict = {}
for fertilizer in fertilizers:
    for direction in fertilizer_to_water:
        if int(direction[1]) <= int(fertilizer) <= int(direction[1]) + int(direction[2]):
            water = int(fertilizer) + int(direction[0])-int((direction[1]))
            water_dict[int(fertilizer)] = water
            break
for fertilizer in fertilizers:
    if int(fertilizer) not in water_dict:
        water_dict[int(fertilizer)] = int(fertilizer)

print(water_dict)
waters = list(water_dict.values())
print(waters)

light_dict = {}
for water in waters:
    for direction in water_to_light:
        if int(direction[1]) <= int(water) <= int(direction[1]) + int(direction[2]):
            light = int(water) + int(direction[0])-int((direction[1]))
            light_dict[int(water)] = light
            break
for water in waters:
    if int(water) not in light_dict:
        light_dict[int(water)] = int(water)

print(light_dict)
lights = list(light_dict.values())
print(lights)

temperature_dict = {}
for light in lights:
    for direction in light_to_temperature:
        if int(direction[1]) <= int(light) <= int(direction[1]) + int(direction[2]):
            temperature = int(light) + int(direction[0])-int((direction[1]))
            temperature_dict[int(light)] = temperature
            break
for light in lights:
    if int(light) not in temperature_dict:
        temperature_dict[int(light)] = int(light)

print(temperature_dict)
temperatures = list(temperature_dict.values())
print(temperatures)

humidity_dict = {}
for temperature in temperatures:
    for direction in temperature_to_humidity:
        if int(direction[1]) <= int(temperature) <= int(direction[1]) + int(direction[2]):
            humidity = int(temperature) + int(direction[0])-int((direction[1]))
            humidity_dict[int(temperature)] = humidity
            break
for temperature in temperatures:
    if int(temperature) not in humidity_dict:
        humidity_dict[int(temperature)] = int(temperature)

print(humidity_dict)
humiditys = list(humidity_dict.values())
print(humiditys)

location_dict = {}
for humidity in humiditys:
    for direction in humidity_to_location:
        if int(direction[1]) <= int(humidity) <= int(direction[1]) + int(direction[2]):
            location = int(humidity) + int(direction[0])-int((direction[1]))
            location_dict[int(humidity)] = location
            break
for humidity in humiditys:
    if int(humidity) not in location_dict:
        location_dict[int(humidity)] = int(humidity)

print(location_dict)
locations = list(location_dict.values())
print(locations)

print(min(locations))
