import random
def start_game():
    
    while True:
        command = menu()
        
        if command == 'q':
            break
        elif command == 'r':
            show_rule()
        elif command == 's':
            new_game()   
    
        

def generate_number():
    return random.randint(1, 100)    

def is_valid(numb):
    flag = True
    try:
        number = int(numb)
    except Exception:
        print('Введите число!')
        flag = False
    
    if flag and not(1 <= number <= 100):
        print('Введите число от 1 до 100!')
        flag = False             
    
    return flag    

def show_rule():
    text = '''
    Загадано целое число от 1 до 100 (включительно).
    Ваша задача угадать число с _ попыток.
    '''
    print(text)

def menu():
    print('Добро пожаловать в игру "Угадай число"')
    print('Опции:')
    print('\tq - выход из игры')
    print('\tr - правила игры')
    print('\ts - начать игру')
    return input('Выберите опцию >> ')
    
       

def check_number(general, current):
    
    if current == general:
        print('Вы угадали, поздравляем!')
        result = True
    elif current < general:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        result = False   
    else:
        print('Ваше число больше загаданного, попробуйте еще разок')
        result = False       
    
    return result    

def new_game():
    gen_number = generate_number()
    count = 0 
    while True:
        
        user_number = input('Ваше число >> ')
        if not is_valid(user_number):
            continue
        
        user_number = int(user_number)
        count += 1
        
        if check_number(gen_number, user_number):
            print(f'количество попыток: {count}')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        else:
            continue
        
start_game()

