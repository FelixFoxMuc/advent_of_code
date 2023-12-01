numbers = []

with open("input.txt", "r") as file:
    for line in file:
        line_digits = []
        start_code = line.strip()
        for value in start_code:
            try:
                digit = int(value)
                line_digits.append(digit)
            except ValueError:
                pass
        line_number = int(f"{line_digits[0]}{line_digits[-1]}")
        numbers.append(line_number)

print(len(numbers))
print(numbers)
print(sum(numbers))

