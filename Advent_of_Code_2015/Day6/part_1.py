# create light_grid
light_grid = {}

for i in range(1000):
    for j in range(1000):
        light_grid[(i, j)] = False

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
                    light_grid[(i, j)] = True
                elif action == "turn off":
                    light_grid[(i, j)] = False
                if action == "toggle":
                    if light_grid[(i, j)]:
                        light_grid[(i, j)] = False
                    else:
                        light_grid[(i, j)] = True

sum_lights_on = 0
for i in range(1000):
    for j in range(1000):
        if light_grid[(i, j)]:
            sum_lights_on += 1

print(sum_lights_on)
