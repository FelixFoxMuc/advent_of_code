total_points = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        card = line.split(": ")[1].split(" | ")
        winning_numbers_raw = card[0].split(" ")
        elf_numbers_raw = card[1].split(" ")

        winning_numbers_int = []
        elf_numbers_int = []
        for string in winning_numbers_raw:
            try:
                digit = int(string)
                winning_numbers_int.append(digit)
            except ValueError:
                pass

        for string in elf_numbers_raw:
            try:
                digit = int(string)
                elf_numbers_int.append(digit)
            except ValueError:
                pass

        card_points = 0

        for digit in elf_numbers_int:
            if digit in winning_numbers_int:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points *= 2

        print(card_points)

        total_points += card_points

print(total_points)
