text_file = open('test51.txt', 'w')
line = input("Enter text: \n")
while line:
    text_file.writelines(line)
    line = input("Enter text: \n")
    if not line:
        break

text_file.close()
text_file = open('test51.txt', 'r')
content = text_file.readlines()
print(content)
text_file.close()
