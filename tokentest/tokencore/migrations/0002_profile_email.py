# Generated by Django 3.1.4 on 2020-12-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokencore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='1@gmail.com', max_length=254),
        ),
    ]
