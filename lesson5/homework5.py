"""
Агеев Георгий BigData 1795
"""
"""
Добавлю две задачи и опишу 5-ую
"""
def num1():
    fin = open('ex1.txt', 'w', encoding='UTF-8')
    data = input('Введите данные для записи в файл или пустую строку: ')
    while data != '':
        fin.write(data + '\n')
        data = input('Введите данные для записи в файл или пустую строку: ')
    fin.close()


def num2(lines=0, words=0):
    fout = open('ex2.txt', encoding='UTF-8')
    for i in fout.readlines():
        print(f"Число слов в строке {lines + 1}: {len(i.split())}")
        lines += 1
    print(f'Число строк: {lines}')
    fout.close()


def num3(i=0, count=0):
    with open('ex3.txt', encoding='UTF-8') as fout:
        for line in fout:
            surname, salary = line.split()
            i += int(salary)
            if int(salary) < 20000:
                print(surname)
            count += 1
        print(f'Средняя величина дохода: {int(i/count)}')



def num4(i=0):
    fout = open('ex4.txt', encoding='UTF-8')
    fin = open('ex4_in.txt', 'w', encoding='UTF-8')
    my_list = ['Один', 'Два', 'Три', 'Четыре']
    for line in fout:
        line = line.split(' - ')
        line[0] = my_list[i]
        fin.write(' - '.join(line))
        i += 1
    fout.close()
    fin.close()


def num5(i=0, sum=0):
    with open('ex5.txt', 'w+', encoding='UTF - 8') as fin:
        fin.write('5 0 1 2 3 7 9 5 6 81 4 56 1')
        fin.seek(0)
        for i in fin.readline().split():
            sum += int(i)
        print(sum)


