from random import randint, choice

container_volumes = []
unique_container_combos = []
eggnog_volume = 150

with open("input.txt", "r") as file:
    for line in file:
        line = int(line.strip())
        container_volumes.append(line)

print(container_volumes)
container_volumes_sorted = sorted(container_volumes)
print(container_volumes_sorted)

container_dict = {}

for i in range(len(container_volumes)):
    container_dict[f"#{i}"] = container_volumes_sorted[i]

print(container_dict)

for k in range(10000000000):
    if k % 100000 == 0:
        print(k)
        print(len(unique_container_combos))
        # From part_1 we know this is the max number of combinations.
        if len(unique_container_combos) == 654:
            break

    for i in range(len(container_volumes)):
        container_dict[f"#{i}"] = container_volumes_sorted[i]
    amount_containers = randint(3, len(container_volumes)-1)

    picked_containers = []
    for j in range(amount_containers):
        container_number = randint(0, len(container_volumes)-1)
        if f"#{container_number}" not in picked_containers:
            picked_containers.append(f"#{container_number}")

    current_volume = 0
    for container in picked_containers:
        current_volume += container_dict[container]

    if current_volume == eggnog_volume:
        sorted_picked_container = sorted(picked_containers)

        if sorted_picked_container not in unique_container_combos:
            unique_container_combos.append(sorted_picked_container)

print(f"Final number of containers: {len(unique_container_combos)}")

min_contatiner = 99
for combo in unique_container_combos:
    if len(combo) < min_contatiner:
        min_contatiner = len(combo)

print(f"Minimum number of container is {min_contatiner}")
number_min_containers = 0
for combo in unique_container_combos:
    if len(combo) == min_contatiner:
        number_min_containers += 1

print(f"The combination number of min_containers is {number_min_containers}")

