# Generated by Django 2.2.14 on 2020-07-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='rejected',
        ),
        migrations.AddField(
            model_name='staff',
            name='studentsaccceptorreject',
            field=models.CharField(default='accept', max_length=10),
        ),
    ]