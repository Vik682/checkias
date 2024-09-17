# Generated by Django 5.1.1 on 2024-09-16 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluator',
            fields=[
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(blank=True, max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('Phone_number', models.IntegerField(blank=True, default=0)),
                ('Num_of_Prelims', models.IntegerField(blank=True, default=0)),
                ('Num_of_Mains', models.IntegerField(blank=True, default=0)),
                ('Num_of_Interviews', models.IntegerField(blank=True, default=0)),
                ('profile_picture', models.ImageField(blank=True, upload_to='storage/user_profile/evaluator/profile_pictures/')),
                ('Rank_secured', models.BooleanField(default=False)),
                ('Medium', models.CharField(choices=[('english', 'English'), ('hindi', 'Hindi')], default='english', max_length=50)),
                ('Optional', models.IntegerField(choices=[(0, 'Not Selected'), (1, 'Agriculture'), (2, 'Animal Husbandry and Veterinary Science'), (3, 'Anthropology'), (4, 'Botany'), (5, 'Chemistry'), (6, 'Civil Engineering'), (7, 'Commerce & Accountancy'), (8, 'Economics'), (9, 'Electrical Engineering'), (10, 'Geography'), (11, 'Geology'), (12, 'History'), (13, 'Law'), (14, 'Management'), (15, 'Mathematics'), (16, 'Mechanical Engineering'), (17, 'Medical Science'), (18, 'Philosophy'), (19, 'Physics'), (20, 'Political Science & International Relations'), (21, 'Psychology'), (22, 'Public Administration'), (23, 'Sociology'), (24, 'Statistics'), (25, 'Zoology'), (26, 'Hindi Literature'), (27, 'Assamese Literature'), (28, 'Bengali Literature'), (29, 'Bodo Literature'), (30, 'Dogri Literature'), (31, 'Gujarati Literature'), (32, 'Kannada Literature'), (33, 'Kashmiri Literature'), (34, 'Konkani Literature'), (35, 'Maithili Literature'), (36, 'Malayalam Literature'), (37, 'Manipuri Literature'), (38, 'Marathi Literature'), (39, 'Nepali Literature'), (40, 'Oriya Literature'), (41, 'Punjabi Literature'), (42, 'Sanskrit Literature'), (43, 'Santhali Literature'), (44, 'Sindhi Literature'), (45, 'Tamil Literature'), (46, 'Telugu Literature'), (47, 'Urdu Literature'), (48, 'English Literature')], default='Not Selected')),
                ('Role', models.CharField(blank=True, choices=[('evaluator', 'Evaluator'), ('Mentor', 'Mentor'), ('Content Creator', 'Content Creator')], max_length=20)),
                ('Evaluation_language', models.CharField(blank=True, choices=[('hindi', 'Hindi'), ('english', 'English')], max_length=20)),
                ('Experience', models.TextField(blank=True)),
                ('Existing_std_email', models.EmailField(blank=True, max_length=254)),
                ('assignment_checked', models.FileField(blank=True, upload_to='storage/user_profile/evaluator/check-pdfs/')),
                ('marksheet', models.FileField(blank=True, upload_to='storage/user_profile/evaluator/marksheet-pdfs/')),
            ],
        ),
    ]
