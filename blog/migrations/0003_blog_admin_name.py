# Generated by Django 2.2.5 on 2021-04-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210416_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='admin_name',
            field=models.CharField(default='', help_text='enter your user name', max_length=1000),
        ),
    ]
