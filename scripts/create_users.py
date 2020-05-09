import random
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

Users = get_user_model()

chars_password = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(_-=+)'
chars_email = 'abcdefghijklmnopqrstuvwxyz'
chars_name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXWYZ'
numbers = '0123456789'

def create_name():
    rNumber = random.randint(1,100)
    return get_random_string(rNumber, chars_name)

def create_password():
    rNumber = random.randint(8,10)
    return get_random_string(rNumber, chars_password)

def create_email():
    rNumber = random.randint(5, 20)
    return get_random_string(rNumber, chars_email)

def create_cpf():
    def insert_number(rNumber, first=True):
        resp = 0
        if first:
            cont = 10
        else:
            cont = 11

        for i in rNumber:
            resp = resp + int(i) * cont
            cont = cont - 1

        resp = resp % 11
        if resp < 2:
            rNumber = rNumber + "0"
        else:
            rNumber = "{}{}".format(rNumber, 11-resp)

        return rNumber

    rNumber = get_random_string(9, numbers)

    rNumber = insert_number(rNumber)
    rNumber = insert_number(rNumber, False)

    return rNumber


def main():
    resp = input('Quantidade de registros? ')
    r = int(resp)

    entry = []
    for i in range(r):
        entry.append(
            Users(
                name="{}".format(create_name()),
                email="{}".format(create_email()),
                password="{}".format(create_password()),
                cpf='{}'.format(create_cpf())
            )
        )

    Users.objects.bulk_create(objs=entry)

if __name__ == "__main__":
    main()
