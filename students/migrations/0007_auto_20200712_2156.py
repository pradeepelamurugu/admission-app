# Generated by Django 2.2.14 on 2020-07-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20200712_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.BooleanField(choices=[('1', 'accept'), ('2', 'reject')], default=1),
        ),
    ]
