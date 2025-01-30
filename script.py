import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj.settings')
django.setup()

from core.models import Person

fake = Faker()

def generate_dummy_data(num_records=500):
    persons = [
        Person(
            name=fake.name(),
            address=fake.address()
        )
        for _ in range(num_records)
    ]

    Person.objects.bulk_create(persons)
    print("Your Data has been added")


if __name__ == "__main__":   
    generate_dummy_data(500)