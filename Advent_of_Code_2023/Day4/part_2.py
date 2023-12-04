total_number_cards = 0

card_list = {}

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        card_name = line.split(":")[0]

        card_index = ""
        for c in card_name:
            if c.isdigit():
                card_index = card_index + c
        card_index = int(card_index)

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

        card_list[card_index] = {"amount": 1, "winning": winning_numbers_int, "elf_numbers": elf_numbers_int}

for index in card_list:
    # print(index)
    current_card = card_list[index]
    current_amount = current_card["amount"]
    winning_numbers = current_card["winning"]
    elf_numbers = current_card["elf_numbers"]

    right_numbers = 0
    for _ in range(current_amount):
        right_numbers = 0
        for number in elf_numbers:
            if number in winning_numbers:
                right_numbers += 1

        for i in range(index+1, index+right_numbers+1):
            try:
                save = card_list[i]["amount"]
                save_1 = save + 1
                card_list[i]["amount"] = save_1
            except KeyError:
                pass

total_sum = 0
for i in range(1, len(card_list)+1):
    # print(card_list[i]["amount"])
    total_sum += card_list[i]["amount"]

print(total_sum)
