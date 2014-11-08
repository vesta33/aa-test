__author__ = 'anastassias'

import Isikukood_new
import datetime
import cProfile
import csv
import codecs
import random

def generate_idcode(number, days):
    startdate = datetime.date(1800,1,1) + datetime.timedelta(days=days)
    year = startdate.year
    first_ten = (str(Isikukood_new.gender(year)) + startdate.strftime('%Y%m%d')[2:] + str(number).zfill(3))
    return first_ten + str(Isikukood_new.control_code(first_ten))

def generate_million():
    codes = []
    #to get 1000000 change j range to 1000 before
    for i in range(1,1000):
            for j in range(0,100):
                codes.append(generate_idcode(i,j))


    print (len(codes))

    with open('users.csv', 'w', encoding='utf-8', newline='') as f:
        try:
            fieldnames = ('SOCIAL_SECURITY_NUMBER', 'FORENAME', 'SURNAME', 'GENDER', 'DATE_OF_BIRTH')
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            headers = dict( (n,n) for n in fieldnames )
            writer.writerow(headers)
            file_read = codecs.open("userNames.csv", "r", "utf-8")

            fornames = []
            lastnames = []
            for line in file_read:
                head, sep, tail = line.partition(', ')
                fornames.append(head)
                lastnames.append(tail[:-2])
            file_read.close()
            gender = ['F', 'M']
            for i in range(len(codes)):
                writer.writerow({ 'SOCIAL_SECURITY_NUMBER':codes[i],
                                  'FORENAME':random.choice(fornames),
                                  'SURNAME':random.choice(lastnames),
                                  'GENDER':random.choice(gender),
                                  'DATE_OF_BIRTH':'%02d.%02d.%s' % (int(codes[i][5:7]), int(codes[i][3:5]),int('19' + codes[i][1:3])),
                                  })
        finally:
            f.close()





if __name__ == '__main__':
    print("Your id code is:", Isikukood_new.generate_random_idcode())

    cProfile.run("generate_million()")