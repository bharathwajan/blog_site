# Generated by Django 2.2.5 on 2021-04-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='inner_img',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='outer_img',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
