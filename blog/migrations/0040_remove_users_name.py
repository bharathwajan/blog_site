# Generated by Django 2.2.5 on 2021-05-17 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_auto_20210517_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
    ]