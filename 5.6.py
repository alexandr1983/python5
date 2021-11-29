text_file = open("test56.txt", "w", encoding="utf-8")
content = text_file.write("Informatika: 100(lec) 50(pr) 20(lab)\nPhisika: 30(lec) - 10(lab)\nPhiskultura: - 30(pr) -")
text_file.close()

result = {}
try:
    with open("test56.txt", "r") as f:
        for line in f:
            subject, numbers = line.split(':')
            subject_sum = sum(int(n) for word in numbers.split() for n in word.split('(') if n.isdigit())
            result[subject] = subject_sum
except Exception as err:
    print("Unexpected error:", err)

print(result)
