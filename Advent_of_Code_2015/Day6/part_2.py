# create light_grid
light_grid = {}

for i in range(1000):
    for j in range(1000):
        light_grid[(i, j)] = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.replace(" through ", ";")

        if "turn on" in line:
            line = line.replace("turn on ", "")
            action = "turn on"
        elif "turn off" in line:
            line = line.replace("turn off ", "")
            action = "turn off"
        elif "toggle" in line:
            line = line.replace("toggle ", "")
            action = "toggle"

        l1 = int(line.split(";")[0].split(",")[0])
        l2 = int(line.split(";")[0].split(",")[1])
        top_left = (l1, l2)

        r1 = int(line.split(";")[1].split(",")[0])
        r2 = int(line.split(";")[1].split(",")[1])
        bottom_right = (r1, r2)

        for i in range(l1, r1+1):
            for j in range(l2, r2+1):
                if action == "turn on":
                    current_brightness = light_grid[(i, j)]
                    light_grid[(i, j)] = current_brightness + 1
                elif action == "turn off":
                    if light_grid[(i, j)] <= 0:
                        pass
                    else:
                        current_brightness = light_grid[(i, j)]
                        light_grid[(i, j)] = current_brightness - 1
                elif action == "toggle":
                    current_brightness = light_grid[(i, j)]
                    light_grid[(i, j)] = current_brightness + 2

sum_lights_on = 0
for i in range(1000):
    for j in range(1000):
        sum_lights_on += light_grid[(i, j)]

print(sum_lights_on)

# Wrong answer: 13660231
