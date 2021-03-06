# Generated by Django 2.1.4 on 2019-01-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20190103_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_num',
            field=models.IntegerField(default=0, verbose_name='Course number'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='student_num',
            field=models.IntegerField(default=0, verbose_name='Student number'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='click_num',
            field=models.IntegerField(default=0, verbose_name='Flick number'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='fav_num',
            field=models.IntegerField(default=0, verbose_name='Favorites number'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='Image'),
        ),
    ]
