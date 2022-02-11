# Generated by Django 2.2.7 on 2022-02-10 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_correctanswer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proints', models.IntegerField(max_length=255)),
                ('correct_answer_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.CorrectAnswer')),
            ],
        ),
    ]