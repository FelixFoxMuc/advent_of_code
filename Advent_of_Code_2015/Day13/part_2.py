from random import shuffle

happiness_dict = {}

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        line_list = line.split(" ")

        person = line_list[0]
        neighbour = line_list[-1].removesuffix(".")
        score = line_list[3]
        if line_list[2] == "gain":
            score = int(score)
        elif line_list[2] == "lose":
            score = -1 * int(score)

        try:
            found_entry = happiness_dict[person]
            happiness_dict[person][neighbour] = int(score)
        except KeyError:
            happiness_dict[person] = {neighbour: score}

guest_seats = [guest for guest in happiness_dict]


for person in guest_seats:
    try:
        found_entry = happiness_dict["Felix"]
        happiness_dict["Felix"][person] = 0
    except KeyError:
        happiness_dict["Felix"] = {person: 0}
    finally:
        happiness_dict[person]["Felix"] = 0

# print(happiness_dict)

guest_seats = [guest for guest in happiness_dict]
max_happiness = 0

for j in range(100000000):
    shuffle(guest_seats)

    happiness = 0
    for i in range(len(guest_seats)):
        try:
            happiness += happiness_dict[guest_seats[i]][guest_seats[i+1]]
            happiness += happiness_dict[guest_seats[-i]][guest_seats[-i-1]]
        except IndexError:
            happiness += happiness_dict[guest_seats[i]][guest_seats[0]]
            happiness += happiness_dict[guest_seats[-i]][guest_seats[-i-1]]

    if happiness > max_happiness:
        max_happiness = happiness
        print(max_happiness)






