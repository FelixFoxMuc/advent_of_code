# Lesson: It will take ages with strings but go very fast with lists :)

sample = "1113122113"
input = [int(char) for char in sample]

output = []

for i in range(50):
    count = 1
    for n in range(len(input)):
        try:
            if input[n] == input[n+1]:
                count += 1
            else:
                output.append(count)
                output.append(input[n])
                count = 1
        except IndexError:
            output.append(count)
            output.append(input[n])

    input = [int(char) for char in output]
    output = []
    print(i)
    print(len(input))

print(len(input))
