__author__ = 'anastassias'
import radar
import random


class PersonIdCode:
    def __init__(self, isikukood):
        self.isikukood = isikukood


def random_date():
    # Generate random datetime (parsing dates from str values)
    date = (radar.random_datetime(start='1800-01-01', stop='2199-01-01'))
    print("Birthdate:", date)
    #print (dir(date))
    #date = str(date)
    return date

def gender(year):
    if 1800 <= year <= 1899:
        gender = random.randint(1, 2)
    elif 1900 <= year <= 1999:
        gender = random.randint(3, 4)
    elif 2000 <= year <= 2099:
        gender = random.randint(5, 6)
    else:
        gender = random.randint(7, 8)
    return gender


def control_code(first_ten):
    kaal_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    kaal_two = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    total = sum(kaal*int(i) for kaal,i in zip(kaal_one,first_ten))
    divisor = total % 11
    if divisor != 10:
         return divisor

    total_two = sum(kaal*int(i) for kaal,i in zip(kaal_one,first_ten))
    divisor = total_two % 11
    if divisor != 10:
        return divisor
    else:
        return 0




def generate_random_idcode():
    a = random_date()
    year = a.year
    first_ten = (str(gender(year)) + a.strftime('%Y%m%d')[2:] + str(random.randint(1, 999)).zfill(3))
    return first_ten + str(control_code(first_ten))

if __name__ == '__main__':
    print("Your id code is:", generate_random_idcode())