# Generated by Django 2.1.4 on 2019-01-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_course_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='objective',
            field=models.CharField(default='', max_length=200, verbose_name='objective'),
        ),
        migrations.AddField(
            model_name='course',
            name='requisite',
            field=models.CharField(default='', max_length=200, verbose_name='requisite'),
        ),
    ]
