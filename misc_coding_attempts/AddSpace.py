text_file = open('1990.txt', 'r')
new_file = open('spaceAdded.txt', 'x')

for line in text_file:
    for i in range(len(line)):
        new_file.write(line[i])
        if (line[i].islower() and line[i + 1].isupper()):
            new_file.write(" " + line[i + 1])
            i += 1
        i += 1

text_file.close()
new_file.close()