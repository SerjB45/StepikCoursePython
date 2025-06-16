a, b = int(input()), int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a ** 10 + b **10) **0.5)


def check_imt(m, h):
    imt = m / h ** 2
    if imt < 18.5:
        print('Недостаточная масса')
    elif imt <= 25:
        print('Оптимальная масса')
    else:
        print('Избыточная масса')        

check_imt(float(input()), float(input()))



def cost_text(text):
    cost = len(text) * 60
    cost_txt = f'{cost // 100} р. {cost % 100} коп.' 
    print(cost_txt)

cost_text(input())




animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", 
           "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
year = int(input())
n = year % 12 - 1
print(animals[n]) 



n = input()
n = n[0] + n[5:0:-1]
n = n[0] + n[len(n):0:-1] if len(n) > 5 else n[::-1]

n = input()[::-1]
n_txt = ''
for i, c in enumerate(n):
    if (i + 1) % 3 == 0:
        n_txt += c + ','
    else:
        n_txt += c 
n_txt = n_txt[::-1].lstrip(',')    
print(n_txt)




coords = [list(map(int,input().split())) for _ in range(int(input()))]

def get_pos(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0

count_cords = [0, 0, 0, 0, 0]
for c in coords:
    n = get_pos(*c)
    count_cords[n] += 1

print(f'Первая четверть: {count_cords[1]}')
print(f'Вторая четверть: {count_cords[2]}')
print(f'Третья четверть: {count_cords[3]}')
print(f'Четвертая четверть: {count_cords[4]}')
        