# Generated by Django 2.2.5 on 2021-05-04 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user',
            new_name='name',
        ),
    ]
