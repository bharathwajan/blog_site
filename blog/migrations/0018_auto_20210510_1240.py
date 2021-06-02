# Generated by Django 2.2.5 on 2021-05-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_self_intro_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='meme',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='paragraph',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
