import os
import django
import random
from app.models import AccessRecord, Webpage, Topic
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project_settings'
                      )
django.setup()
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fake.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url,
                                              name=fake_name)
        acc_rec = AccessRecord.Objects.get_or_create(name=webpg,
                                                     date=fake_date)[0]


if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete!')
