# Generated by Django 2.2.5 on 2021-04-23 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_admin_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='admin_name',
            new_name='blogger_name',
        ),
    ]
