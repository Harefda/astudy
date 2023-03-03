# Generated by Django 3.1.7 on 2021-03-07 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210307_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='duration_time',
        ),
        migrations.CreateModel(
            name='CourseDurationTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(default=0)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='duration_time', to='courses.course')),
            ],
        ),
    ]