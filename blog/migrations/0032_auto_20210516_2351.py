# Generated by Django 2.2.5 on 2021-05-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20210516_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='inter_para_img',
            new_name='final_img',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='outer_img',
        ),
        migrations.AddField(
            model_name='blog',
            name='final_paragraph',
            field=models.TextField(blank=True, help_text='Dont use this field if you want to put meme or video else it may cause error'),
        ),
        migrations.AddField(
            model_name='blog',
            name='first_img',
            field=models.ImageField(blank=True, help_text='This image will be displayed on the middle of the paragraph', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='blog',
            name='inter_img',
            field=models.ImageField(blank=True, help_text='This image will be displayed on the middle of the paragraph', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='blog',
            name='paragraph2',
            field=models.TextField(blank=True, help_text='Dont use this field if you want to put meme or video else it may cause error'),
        ),
    ]