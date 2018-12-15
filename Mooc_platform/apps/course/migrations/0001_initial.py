# Generated by Django 2.1.2 on 2018-12-15 01:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Course name')),
                ('desc', models.CharField(max_length=50, verbose_name='Course description')),
                ('detail', models.TextField(verbose_name='Course detail')),
                ('difficulty', models.CharField(choices=[('el', 'Elementary'), ('in', 'Intermediate'), ('ad', 'Advanced')], max_length=2, verbose_name='Difficulty')),
                ('study_time', models.IntegerField(default=0, verbose_name='Study time (min)')),
                ('student_nums', models.IntegerField(default=0, verbose_name='Student number')),
                ('favor_nums', models.IntegerField(default=0, verbose_name='Favor number')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='Cover image')),
                ('click_nums', models.IntegerField(default=0, verbose_name='Click number')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Course resource name')),
                ('download', models.FileField(upload_to='courses/resources/%Y/%m', verbose_name='Resource file')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Course resource',
                'verbose_name_plural': 'Course resources',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Lesson name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Video name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='Lesson')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
    ]
