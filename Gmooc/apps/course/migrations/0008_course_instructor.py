# Generated by Django 2.1.4 on 2019-01-06 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_instructor_image'),
        ('course', '0007_video_study_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='organization.Instructor', verbose_name='Instructor'),
            preserve_default=False,
        ),
    ]