__author__ = 'anastassias'
import radar
from random import randint
import random

class PersonIdCode:
    def __init__(self, isikukood):
        self.isikukood = isikukood


def random_date():
     # Generate random datetime (parsing dates from str values)
    date = (radar.random_datetime(start='1800-01-01', stop='2199-01-01'))
    print ("Birthdate:", date)
    date = str(date)
    return date

a = random_date()
year = a.split('-', 1)[0].replace('', '').upper()
month = a.split('-', 2)[1].replace('', '').upper()
day = a.split('-', 3)[2].replace('', '').upper()

def gender():
    if 1800 <= int(year) <= 1899:
        genger = randint(1,2)
    elif 1900 <= int(year) <= 1999:
        genger = randint(3,4)
    elif 2000 <= int(year) <= 2099:
        genger = randint(5,6)
    else:
        genger = randint(7,8)
    return genger


first_ten = (str(gender()) + year[2:4] + month + day + str(random.randint(1,9)) + str(random.randint(0,9)) + str(random.randint(0,9)))

def generate_random_idcode():
    return (first_ten + str(control_code()))

def control_code():
    kaal_one = [1,2,3,4,5,6,7,8,9,1]
    kaal_two = [3,4,5,6,7,8,9,1,2,3]
    total = 0
    total_two = 0
    for i in first_ten:
        for j in kaal_one:
            total += int(i) * kaal_one[j]
            divisor = total % 11
    if (divisor == 10):
            for k in kaal_two:
                total_two += int(i) * kaal_two[k]
                divisor = total_two % 11
                if (divisor != 10):
                    return divisor
                else:
                    return 0
    elif (divisor != 10):
                return divisor



print ("Your id code is:", generate_random_idcode())