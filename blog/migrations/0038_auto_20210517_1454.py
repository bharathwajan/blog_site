# Generated by Django 2.2.5 on 2021-05-17 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20210517_1432'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='subscribers',
        ),
    ]