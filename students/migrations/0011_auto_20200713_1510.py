# Generated by Django 2.2.14 on 2020-07-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20200713_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[(True, 'accept'), (False, 'reject')], default='reject', max_length=30),
        ),
    ]
