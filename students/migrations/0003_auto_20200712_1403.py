# Generated by Django 2.2.14 on 2020-07-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('1', 'accept'), ('2', 'reject')], max_length=30),
        ),
    ]
