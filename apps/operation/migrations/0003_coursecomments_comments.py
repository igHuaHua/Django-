# Generated by Django 2.2.2 on 2019-08-13 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_usercourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecomments',
            name='comments',
            field=models.CharField(default='', max_length=200, verbose_name='评论'),
        ),
    ]
