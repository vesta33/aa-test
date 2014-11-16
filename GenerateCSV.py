__author__ = 'anastassias'

import Isikukood_new
import datetime
import cProfile
import csv
import random


def generate_idcode(number, days):
    # for each day generates from 1 to 1000 (j) generates random number from 1 to 999
    startdate = datetime.date(1800, 1, 1) + datetime.timedelta(days=days)
    year = startdate.year
    first_ten = (str(Isikukood_new.gender(year)) + startdate.strftime('%Y%m%d')[2:] + str(number).zfill(3))
    return first_ten + str(Isikukood_new.control_code(first_ten))


def read_file(file):
    with open(file, 'r', encoding='utf-8') as file_read:
        forname = []
        lastname = []

        for line in file_read:
            head, sep, tail = line.partition(', ')
            forname.append(head)
            lastname.append(tail[:-1])
    return forname, lastname


# print (read_file('userNames.csv'))

def generate_million():
    with open('users.csv', 'w', encoding='utf-8', newline='') as f:

        fieldnames = ('SOCIAL_SECURITY_NUMBER', 'FORENAME', 'SURNAME', 'GENDER', 'DATE_OF_BIRTH')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        headers = dict((n, n) for n in fieldnames)
        writer.writerow(headers)

        fornames, lastnames = read_file('userNames.csv')

        gender = ['F', 'M']
        # to get 1000000 change j range to 1000 before
        for i in range(1, 1000):
            for j in range(0, 10):
                writer.writerow({
                    'SOCIAL_SECURITY_NUMBER': generate_idcode(i, j),
                    'FORENAME': random.choice(fornames),
                    'SURNAME': random.choice(lastnames),
                    'GENDER': random.choice(gender),
                    'DATE_OF_BIRTH': '%02d.%02d.%02d' % (
                        int(generate_idcode(i, j)[5:7]), int(generate_idcode(i, j)[3:5]), 00),
                })


if __name__ == '__main__':
    print("Your id code is:", Isikukood_new.generate_random_idcode())

    cProfile.run("generate_million()")
#To control uniqueness use: awk -F "," '{print $1}' myfile.csv | uniq -D