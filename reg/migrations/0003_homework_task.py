# Generated by Django 5.0.1 on 2024-02-14 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_course_homework_user_delete_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='task',
            field=models.CharField(default='Какое-то домашнее задание'),
        ),
    ]
