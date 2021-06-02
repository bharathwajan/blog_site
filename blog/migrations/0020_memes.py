# Generated by Django 2.2.5 on 2021-05-10 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_auto_20210510_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='memes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='pics')),
                ('description', models.TextField(blank=True)),
                ('posted_on', models.DateField()),
                ('blogger_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
