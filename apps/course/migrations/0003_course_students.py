# Generated by Django 2.2.2 on 2019-08-13 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_courseresourse_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
    ]
