seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

source_file = "input.txt"

source = ""

with open(source_file, "r") as file:
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
            value = line.split(" ")
            value_list = [int(a) for a in value]
            seed_to_soil.append(value_list)

        elif source == "soil-to-fertilizer":
            value = line.split(" ")
            value_list = [int(a) for a in value]
            soil_to_fertilizer.append(value_list)

        elif source == "fertilizer-to-water":
            value = line.split(" ")
            value_list = [int(a) for a in value]
            fertilizer_to_water.append(value_list)

        elif source == "water-to-light":
            value = line.split(" ")
            value_list = [int(a) for a in value]
            water_to_light.append(value_list)

        elif source == "light-to-temperature":
            value = line.split(" ")
            value_list = [int(a) for a in value]
            light_to_temperature.append(value_list)

        elif source == "temperature-to-humidity":
            value = line.split(" ")
            value_list = [int(a) for a in value]
            temperature_to_humidity.append(value_list)

        elif source == "humidity-to-location":
            value = line.split(" ")
            value_list = [int(a) for a in value]
            humidity_to_location.append(value_list)

seed_ranges = []

with open(source_file, "r") as file:
    for line in file:
        line = line.strip()

        if "seeds" in line:
            seeds_instructions = line.split(" ")[1:]

    seeds_instructions = [int(i) for i in seeds_instructions]

    for i in range(len(seeds_instructions)):
        if i % 2 == 0:
            start = seeds_instructions[i]
            end = start + seeds_instructions[i + 1]

            seed_range = (start, end)
            seed_ranges.append(seed_range)

    print(seed_ranges)
#
# print(seeds)
# print(seed_to_soil)
# print(soil_to_fertilizer)
# print(fertilizer_to_water)
# print(water_to_light)
# print(light_to_temperature)
# print(temperature_to_humidity)
# print(humidity_to_location)

for i in range(100000000000000000000000):
    if i % 100000 == 0:
        print(f"Checking {i}")
    # location to humidity
    humidity_set = False
    for routes in humidity_to_location:
        if i in range(routes[0], routes[0] + routes[2]):
            humidity = routes[1] - routes[0] + i
            humidity_set = True
    if not humidity_set:
        humidity = i

    # humidity to temp
    temperature_set = False
    for routes in temperature_to_humidity:
        if humidity in range(routes[0], routes[0] + routes[2]):
            temperature = routes[1] - routes[0] + humidity
            temperature_set = True
    if not temperature_set:
        temperature = humidity

    # temp to light
    light_set = False
    for routes in light_to_temperature:
        if temperature in range(routes[0], routes[0] + routes[2]):
            light = routes[1] - routes[0] + temperature
            light_set = True
    if not light_set:
        light = temperature

    # light to water
    water_set = False
    for routes in water_to_light:
        if light in range(routes[0], routes[0] + routes[2]):
            water = routes[1] - routes[0] + light
            water_set = True
    if not water_set:
        water = light

    # water to fertilizer
    fertilizer_set = False
    for routes in fertilizer_to_water:
        if water in range(routes[0], routes[0] + routes[2]):
            fertilizer = routes[1] - routes[0] + water
            fertilizer_set = True
    if not fertilizer_set:
        fertilizer = water

    # fertilizer to soil
    soil_set = False
    for routes in soil_to_fertilizer:
        if fertilizer in range(routes[0], routes[0] + routes[2]):
            soil = routes[1] - routes[0] + fertilizer
            soil_set = True
    if not soil_set:
        soil = fertilizer

    # soil to seed
    seed_set = False
    for routes in seed_to_soil:
        if soil in range(routes[0], routes[0] + routes[2]):
            seed = routes[1] - routes[0] + soil
            seed_set = True
    if not seed_set:
        seed = soil

    # print(f"humidity: {humidity}")
    # print(f"temp: {temperature}")
    # print(f"light: {light}")
    # print(f"water: {water}")
    # print(f"fertilizer: {fertilizer}")
    # print(f"soil: {soil}")
    # print(f"seed: {seed}")
    for ranges in seed_ranges:
        if seed in range(ranges[0], ranges[1]):
            print(f"The minimum location is: {i}")
            exit("Success")
