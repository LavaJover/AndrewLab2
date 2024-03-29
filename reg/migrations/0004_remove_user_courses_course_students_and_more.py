# Generated by Django 5.0.1 on 2024-02-16 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_homework_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='reg.user'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(verbose_name='Название дисциплины'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(verbose_name='Фамилия пользователя'),
        ),
        migrations.CreateModel(
            name='HomeworkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Тема')),
                ('task', models.TextField(default='Какое-то домашнее задание', verbose_name='Задание')),
                ('deadline', models.DateTimeField(verbose_name='Срок сдачи')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.course')),
            ],
        ),
        migrations.CreateModel(
            name='HwDone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, verbose_name='Содержание')),
                ('mark', models.IntegerField(verbose_name='Оценка')),
                ('hw_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.homeworktype')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.user', verbose_name='Студент')),
            ],
        ),
        migrations.DeleteModel(
            name='Homework',
        ),
    ]
