# Generated by Django 4.2.4 on 2023-12-09 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_student_classrooms_classroom_teacher_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='classrooms',
            new_name='students',
        ),
    ]
