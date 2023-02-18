# Generated by Django 3.0 on 2023-02-15 16:15

from django.db import migrations

from lettings.models import Address
from oc_lettings_site import models


def import_addresses(apps, schema):
    old_adress = apps.get_model('oc_lettings_site', 'Address')
    new_adresses = apps.get_model('lettings', 'Address')
    old_addresses = old_adress.objects.all()
    for address in old_addresses:
        print(address.__dict__)
        del address._state
        new_address = Address(**address.__dict__)
        new_address.save()


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0002_auto_20230215_1709'),
    ]

    operations = [
        migrations.RunPython(import_addresses),
    ]
