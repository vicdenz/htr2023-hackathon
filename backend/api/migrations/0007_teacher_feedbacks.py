# Generated by Django 4.2.4 on 2023-12-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_studentclassroom_studentfeedback_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='feedbacks',
            field=models.ManyToManyField(to='api.customfeedback'),
        ),
    ]
