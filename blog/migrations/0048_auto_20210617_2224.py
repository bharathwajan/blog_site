# Generated by Django 2.2.5 on 2021-06-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_auto_20210617_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sub_topic_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='sub_topic_final',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]