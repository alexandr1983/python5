with open('test54.txt', 'r') as my_file:
    a = []
    b = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           b.append(i[0])
        a.append(i[1])
print(f"> 20.000 {b} ")
print(f"Srednii dohod {sum(map(int, a)) / len(a)}")
