import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proTwo.settings')

import django
django.setup()

# FAKE emails

import random
from appTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for i in range(N):
        fake_first = fakegen.first_name()
        fake_last  = fakegen.last_name()
        fake_email = fakegen.ascii_free_email()
        usInfo= User.objects.get_or_create(first_name = fake_first, last_name= fake_last, email = fake_email)[0]

if __name__ == '__main__':
    print('populating script!!')
    populate(10)
    print('complete')
