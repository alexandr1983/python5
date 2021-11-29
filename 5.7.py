import json
text_file = open('test57.txt', 'w', encoding='utf-8')
content = text_file.write("firm_1   ООО   13000   5088\nfirm_2   ООО   10500   5000\nfirm_3   ООО   10500   5800\nfirm_4   ООО   18000   5000\nfirm_5   ООО   10008   5009\n")
text_file.close()

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('test57.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('test57.json', 'w', encoding='utf-8') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
