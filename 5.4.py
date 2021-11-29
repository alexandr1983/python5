text_file = open("test541.txt", "w", encoding="utf-8")
content = text_file.write("One - 1\nTwo - 2\nThree - 3\nFour - 4\n")
text_file.close()

tran = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
a = []

try:
    text_file = open("test541.txt", "r")
    for i in text_file:
        k = i.split(" - ")
        print(k)
        if k[0] in tran:
            w = tran[k[0]]
            a.append(w +' - '+ k[1])
    print(a)
finally:
    text_file.close()

try:
    text_file = open("test542.txt", "w")
    text_file.writelines(a)
finally:
    text_file.close()
