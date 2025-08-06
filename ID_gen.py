import random


def generate_random_area_code():
    file = open('./area_code.txt', 'r', encoding='utf-8')
    lines = file.readlines()

    address = lines[random.randint(0, len(lines) - 1)]
    code_address = address.split(',')
    area_code = address.split(',')[0]
    address_name = address.split(',')[1]
    # print(address_code)
    return code_address

def generate_random_birthday_date():
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = random.randint(1950, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, days[month - 1])
    birthday_date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)

    return birthday_date

def generate_random_sequence_code():
    sequence_code = str(random.randint(1, 999)).zfill(3)

    return sequence_code

def generate_check_code(body):
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code_dict = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    check_code = sum(int(body[i]) * factors[i] for i in range(len(body))) % 11

    return check_code_dict[check_code]

def generate_random_id():
    code_and_address = generate_random_area_code()
    area_code = code_and_address[0]
    address_name = code_and_address[1]
    birthday_date = generate_random_birthday_date()
    sequence_code = generate_random_sequence_code()
    body = area_code + birthday_date + sequence_code
    check_code = generate_check_code(body)
    id_number = body + check_code
    result = id_number  + ', ' + address_name

    return result

for i in range(5):
    id_and_address = generate_random_id()
    print(id_and_address)
