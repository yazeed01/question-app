# Generated by Django 2.2.7 on 2022-02-10 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220210_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correctanswer',
            name='question',
        ),
    ]
