input = "1113122113"
output = ""

for i in range(40):
    count = 1
    for n in range(len(input)):
        try:
            if input[n] == input[n+1]:
                count += 1
            else:
                output += str(count)
                output += input[n]
                count = 1
        except IndexError:
            output += str(count)
            output += input[n]

    input = output
    output = ""
    print(i)
    print(len(input))

print(len(input))
