# Generated by Django 5.0.1 on 2024-02-16 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0004_remove_user_courses_course_students_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Student',
        ),
    ]