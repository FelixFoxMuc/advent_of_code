deers = {}

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")
        name = line[0]
        speed = line[3]
        duration = line[6]
        rest = line[-2]
        next_rest = int(duration)
        fly = True
        next_fly = int(duration) + int(rest)
        deers[name] = {"speed": int(speed), "duration": int(duration), "rest": int(rest), "next_rest": next_rest,
                       "next_fly": next_fly, "fly": fly, "distance": 0, "points": 0}


print(line)
print(deers)

race_time = 2503

for i in range(race_time):
    for deer in deers:
        distance = deers[deer]["distance"]
        speed = deers[deer]["speed"]
        duration = deers[deer]["duration"]
        rest = deers[deer]["rest"]
        next_rest = deers[deer]["next_rest"]
        next_fly = deers[deer]["next_fly"]
        fly = deers[deer]["fly"]

        if i == next_rest:
            deers[deer]["fly"] = False
            deers[deer]["next_rest"] += (duration + rest)
            fly = False
        elif i == next_fly:
            deers[deer]["next_fly"] += (duration + rest)
            deers[deer]["fly"] = True
            fly = True

        if fly:
            distance += speed

        deers[deer]["distance"] = distance

    # current_distances = []
    current_distances = [deers[deer]["distance"] for deer in deers]
    max_current_distance = max(current_distances)

    for deer in deers:
        if deers[deer]["distance"] == max_current_distance:
            deers[deer]["points"] += 1

print(deers)
end_points = [deers[deer]["points"] for deer in deers]
for deer in deers:
    if max(end_points) == deers[deer]["points"]:
        print(deer, deers[deer])


