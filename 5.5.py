def summa():
    try:
        with open('test55.txt', 'w+') as a:
            l = input("Enter numbers: \n")
            a.writelines(l)
            n = l.split()
            print(sum(map(float, n)))
    except ValueError:
        print('ValueError')
summa()
