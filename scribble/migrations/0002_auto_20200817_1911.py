# Generated by Django 3.1 on 2020-08-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scribble', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(default='SOME STRING', max_length=1000),
        ),
    ]
