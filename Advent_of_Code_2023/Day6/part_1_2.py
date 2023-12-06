times = []
distances = []
acceleration = 1
winning_list = []

with open("input2.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")

        if "Time:" in line:
            for item in line:
                try:
                    times.append(int(item))
                except ValueError:
                    pass
                finally:
                    pass

        if "Distance:" in line:
            for item in line:
                try:
                    distances.append(int(item))
                except ValueError:
                    pass
                finally:
                    pass

for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    wins = []
    for j in range(time):
        speed = j * acceleration
        remaining_time = time - j
        if speed*remaining_time > distance:
            wins.append(j)
    amount_wins = len(wins)
    winning_list.append(amount_wins)

print(winning_list)

factor = 1
for num in winning_list:
    factor *= num

print(factor)



