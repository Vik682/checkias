# Generated by Django 5.1.1 on 2024-09-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Student'), (2, 'Coaching'), (3, 'Evaluator'), (4, 'Reviewer'), (5, 'Enquiry'), (6, 'Admin'), (7, 'Superuser')]),
        ),
    ]
