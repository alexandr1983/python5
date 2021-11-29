import random

def numbers(file):
    count = random.randint(20, 100)
    try:
        with open(file, 'w') as f:
            for _ in range(count):
                f.write(' '.join([str(i) for i in random.sample(range(11, 80), random.randint(7, 23))]))
                f.write('\n')
    except Exception as err:
        print('Unexpected error:', err)


def summa(file):
    k = 0
    try:
        with open(file, "r") as f:
            for j in f:
                try:
                    k += sum([float(x) for x in j.split()])
                except ValueError as err:
                    print("ValueError:", err)
    except Exception as err:
        print('Unexpected error:', err)
    return k


numbers('test56.txt')
print(f"Summa: {summa('test56.txt')}")
