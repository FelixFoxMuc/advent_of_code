spelled_digits = {"one": 1, "two": 2, "three": 3, "four": 4,
                  "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

numbers = []

#open sample
with open("input.txt", "r") as file:
    #iterate through every line
    for line in file:
        line = line.strip()
        # find first digit
        found_first = 0
        i = 0
        while found_first == 0:
            try:
                first_digit = int(line[i])
                found_first = 1
            except ValueError:
                partial_text = ""
                for a in range(i+1):
                    partial_text += line[a]
                for key in spelled_digits:
                    if key in partial_text:
                        first_digit = spelled_digits[key]
                        found_first = 1
                i += 1

        # find second digit
        found_second = 0
        i = 0
        while found_second == 0:
            try:
                second_digit = int(line[(-1)*(i+1)])
                found_second = 1
            except ValueError:
                partial_text = ""
                for a in range(i + 1):
                    partial_text = line[-(a+1)] + partial_text
                for key in spelled_digits:
                    if key in partial_text:
                        second_digit = spelled_digits[key]
                        found_second = 1
                i += 1

        # merge together both digits to one numer
        line_number = int(f"{first_digit}{second_digit}")
        # append number to numbers
        numbers.append(line_number)
print(len(numbers))
print(numbers)
print(sum(numbers))
