deers = {}
distances = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")
        name = line[0]
        speed = line[3]
        duration = line[6]
        rest = line[-2]
        deers[name] = {"speed": int(speed), "duration": int(duration), "rest": int(rest)}


print(line)
print(deers)

race_time = 2504

for deer in deers:
    distance = 0
    speed = deers[deer]["speed"]
    duration = deers[deer]["duration"]
    rest = deers[deer]["rest"]
    next_rest = duration
    next_fly = duration + rest
    fly = True
    time_remain = race_time

    for i in range(race_time):
        if i == next_rest:
            fly = False
            next_rest += (duration + rest)
        elif i == next_fly:
            next_fly += (duration + rest)
            fly = True

        if fly:
            distance += speed

    deers[deer]["distance"] = distance
    distances.append(distance)

print(deers)
print(max(distances))

