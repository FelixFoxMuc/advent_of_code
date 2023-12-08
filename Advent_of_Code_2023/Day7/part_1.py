cards = {}

symbols = {"A": "A", "K": "B", "Q": "C", "J": "D", "T": "E", "9": "F", "8": "G", "7": "H", "6": "I", "5": "J", "4": "K", "3": "L", "2": "M"}

with open("input.txt", "r") as file:
    for line in file:
        key = ""
        line = line.strip().split(" ")
        for char in line[0]:
            key += symbols[char]
        cards[key] = {"value": line[1], "card_type": ""}

print(cards)
print(len(cards))

card_num_symbols = []

five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pair = []
one_pair = []
high_card = []

for card in cards:
    number_symbols = []
    for symbol in symbols.values():
        num_symbol = card.count(symbol)
        number_symbols.append(num_symbol)
        number_symbols = [num for num in number_symbols if num > 0]
    print(number_symbols, card)

    if max(number_symbols) == 5:
        five_of_kind.append(card)
    elif max(number_symbols) == 4:
        four_of_kind.append(card)
    elif max(number_symbols) == 3 and min(number_symbols) == 2:
        full_house.append(card)
    elif max(number_symbols) == 3:
        three_of_kind.append(card)
    elif max(number_symbols) == 2 and number_symbols.count(2) == 2:
        two_pair.append(card)
    elif max(number_symbols) == 2:
        one_pair.append(card)
    else:
        high_card.append(card)

print(len(five_of_kind), five_of_kind)
print(len(four_of_kind), four_of_kind)
print(len(full_house), full_house)
print(len(three_of_kind), three_of_kind)
print(len(two_pair), two_pair)
print(len(one_pair), one_pair)
print(len(high_card), high_card)

# sort each deck of cards and then merge them again for calculation

sort_five_of_kind = sorted(five_of_kind)
sort_four_of_kind = sorted(four_of_kind)
sort_full_house = sorted(full_house)
sort_three_of_kind = sorted(three_of_kind)
sort_two_pair = sorted(two_pair)
sort_one_pair = sorted(one_pair)
sort_high_card = sorted(high_card)


sorted_all = sort_five_of_kind + sort_four_of_kind + sort_full_house + sort_three_of_kind + sort_two_pair + sort_one_pair + sort_high_card

sorted_all.reverse()

print(sorted_all)

sum_card_values = 0
i = 1
for x in sorted_all:
    value_card = int(cards[x]["value"]) * i
    sum_card_values += value_card
    i += 1

print(sum_card_values)


print("solution from solution: 249483956")