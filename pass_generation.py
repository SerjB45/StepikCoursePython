import random

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
    
def run():
    params = get_parameters() 
    chars = set_template(params)
    passwords = generate_password(params[0], params[1], chars)
    print(*passwords, sep='\n')
    
def get_parameters():
    parameters_pass = []
    parameters_pass.append(int(input('Количество паролей: ')))
    parameters_pass.append(int(input('Длина пароля: ')))
    parameters_pass.append(input('Включать цифры (y\\n): '))
    parameters_pass.append(input('Включать прописные буквы (y\\n): '))
    parameters_pass.append(input('Включать строчные буквы (y\\n): '))
    parameters_pass.append(input('Включать спецсимволы (y\\n): '))
    
    for i in range(2, len(parameters_pass)):
        if parameters_pass[i] == 'y':
            parameters_pass[i] = True
        else:    
            parameters_pass[i] = False
    
    return parameters_pass       

def set_template(params):
    chars = ''
    if params[2] == True:
        chars += digits
    if params[3] == True:
        chars += uppercase_letters
    if params[4] == True:
        chars += lowercase_letters
    if params[5] == True:
        chars += punctuation
    
                
    return chars

def generate_password(qantity, length, chars):
    passwords = []
    for i in range(qantity):
        password = ''
        for _ in range(length):
            password += chars[random.randint(0, len(chars) - 1)]
        
        passwords.append(password)
        
    return passwords

run()