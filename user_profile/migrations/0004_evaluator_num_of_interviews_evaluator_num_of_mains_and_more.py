# Generated by Django 5.1.1 on 2024-09-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_remove_evaluator_attempt_remove_reviewer_attempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluator',
            name='Num_of_Interviews',
            field=models.IntegerField(blank=True, default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='evaluator',
            name='Num_of_Mains',
            field=models.IntegerField(blank=True, default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='evaluator',
            name='Num_of_Prelims',
            field=models.IntegerField(blank=True, default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='evaluator',
            name='optional',
            field=models.CharField(choices=[('agriculture', 'Agriculture'), ('animal husbandry and veterinary science', 'Animal Husbandry and Veterinary Science'), ('anthropology', 'Anthropology'), ('botany', 'Botany'), ('chemistry', 'Chemistry'), ('civil engineering', 'Civil Engineering'), ('commerce & accountancy', 'Commerce & Accountancy'), ('economics', 'Economics'), ('electrical engineering', 'Electrical Engineering'), ('geography', 'Geography'), ('geology', 'Geology'), ('history', 'History'), ('law', 'Law'), ('management', 'Management'), ('mathematics', 'Mathematics'), ('mechanical engineering', 'Mechanical Engineering'), ('medical science', 'Medical Science'), ('philosophy', 'Philosophy'), ('physics', 'Physics'), ('political science & international relations', 'Political Science & International Relations'), ('psychology', 'Psychology'), ('public administration', 'Public Administration'), ('sociology', 'Sociology'), ('statistics', 'Statistics'), ('zoology', 'Zoology'), ('hindi literature', 'Hindi Literature'), ('assamese literature', 'Assamese Literature'), ('bengali literature', 'Bengali Literature'), ('bodo literature', 'Bodo Literature'), ('dogri literature', 'Dogri Literature'), ('gujarati literature', 'Gujarati Literature'), ('kannada literature', 'Kannada Literature'), ('kashmiri literature', 'Kashmiri Literature'), ('konkani literature', 'Konkani Literature'), ('maithili literature', 'Maithili Literature'), ('malayalam literature', 'Malayalam Literature'), ('manipuri literature', 'Manipuri Literature'), ('marathi literature', 'Marathi Literature'), ('nepali literature', 'Nepali Literature'), ('oriya literature', 'Oriya Literature'), ('punjabi literature', 'Punjabi Literature'), ('sanskrit literature', 'Sanskrit Literature'), ('santhali literature', 'Santhali Literature'), ('sindhi literature', 'Sindhi Literature'), ('tamil literature', 'Tamil Literature'), ('telugu literature', 'Telugu Literature'), ('urdu literature', 'Urdu Literature'), ('english literature', 'English Literature')], default='Not Selected', max_length=90),
        ),
        migrations.AddField(
            model_name='evaluator',
            name='rank_secured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='evaluator',
            name='phone_number',
            field=models.IntegerField(blank=True, default=0, max_length=11),
        ),
    ]
