# Generated by Django 2.2.5 on 2021-05-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210509_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='self_intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='pics')),
                ('bio', models.TextField()),
            ],
        ),
    ]
