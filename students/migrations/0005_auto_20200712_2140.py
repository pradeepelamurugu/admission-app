# Generated by Django 2.2.14 on 2020-07-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20200712_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.BooleanField(choices=[('1', 'accept'), ('2', 'reject')]),
        ),
    ]
