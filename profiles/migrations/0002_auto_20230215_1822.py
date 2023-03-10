# Generated by Django 3.0 on 2023-02-15 17:22

from django.db import migrations

from profiles.models import Profile


def import_profile(apps, schema):
    old_profile = apps.get_model('oc_lettings_site', 'Profile')
    old_profiles = old_profile.objects.all()
    for profile in old_profiles:
        del profile._state
        new_profile = Profile(**profile.__dict__)
        new_profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0003_auto_20230215_1821')
    ]

    operations = [
        migrations.RunPython(import_profile),
    ]
