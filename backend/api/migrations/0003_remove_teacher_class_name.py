# Generated by Django 4.2.4 on 2023-12-09 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_teacher_grade_level_student_grade_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='class_name',
        ),
    ]
