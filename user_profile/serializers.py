from rest_framework import serializers
from django.contrib.auth import get_user_model

#import user 
User = get_user_model()

# Profile of Student
class StudentSerializer(serializers.Serializer):
    STATUS_CHOICES = [
        ('2026', '2026'),
        ('2027', '2027'),
        ('after 2027', 'After 2027'),
    ]
    MEDIUM_CHOICES = [
        ('english', 'English'),
        ('hindi', 'Hindi'),
    ]
    name = serializers.CharField(max_length=30, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    attempt = serializers.ChoiceField(choices=STATUS_CHOICES, default='2026')
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    medium = serializers.ChoiceField(choices=MEDIUM_CHOICES, default='english')
    profile_image = serializers.ImageField( required=False)
    courseenroll = serializers.CharField(max_length=1000, required=False)

  
# Profile of Coaching
class CoachingSerializer(serializers.Serializer):
    STATUS_CHOICES = [
        ('2026', '2026'),
        ('2027', '2027'),
        ('after 2027', 'After 2027'),
    ]
    MEDIUM_CHOICES = [
        ('english', 'English'),
        ('hindi', 'Hindi'),
    ]
    name = serializers.CharField(max_length=30, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    attempt = serializers.ChoiceField(choices=STATUS_CHOICES, default='2026')
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    medium = serializers.ChoiceField(choices=MEDIUM_CHOICES, default='english')
    profile_image = serializers.ImageField( required=False)
    courseenroll = serializers.CharField(max_length=1000, required=False)


# Profile of Evaluator
class EvaluatorSerializer(serializers.Serializer):
    medium=[('english','English'),
          ('hindi','Hindi')]
    role=[('evaluator','Evaluator'),
        ('Mentor','Mentor'),
        ('Content Creator','Content Creator')]
    languages=[
    ('hindi','Hindi'),
    ('english','English'),
    ]
    option_sub=[
    ('agriculture', 'Agriculture'),
    ('animal husbandry and veterinary science',  'Animal Husbandry and Veterinary Science'),
    ('anthropology',  'Anthropology'),
    ('botany',  'Botany'),
    ('chemistry',  'Chemistry'),
    ('civil engineering', 'Civil Engineering'),
    ('commerce & accountancy', 'Commerce & Accountancy'),
    ('economics', 'Economics'),
    ('electrical engineering',  'Electrical Engineering'),
    ('geography', 'Geography'),
    ('geology', 'Geology'),
    ('history',  'History'),
    ('law', 'Law'),
    ('management',  'Management'),
    ('mathematics',  'Mathematics'),
    ('mechanical engineering',  'Mechanical Engineering'),
    ('medical science', 'Medical Science'),
    ('philosophy',  'Philosophy'),
    ('physics',  'Physics'),
    ('political science & international relations',  'Political Science & International Relations'),
    ('psychology', 'Psychology'),
    ('public administration',  'Public Administration'),
    ('sociology',  'Sociology'),
    ('statistics', 'Statistics'),
    ('zoology',  'Zoology'),
    ('hindi literature',  'Hindi Literature'),
    ('assamese literature', 'Assamese Literature'),
    ('bengali literature',  'Bengali Literature'),
    ('bodo literature',  'Bodo Literature'),
    ('dogri literature', 'Dogri Literature'),
    ('gujarati literature',  'Gujarati Literature'),
    ('kannada literature',  'Kannada Literature'),
    ('kashmiri literature',  'Kashmiri Literature'),
    ('konkani literature',  'Konkani Literature'),
    ('maithili literature',  'Maithili Literature'),
    ('malayalam literature',  'Malayalam Literature'),
    ('manipuri literature',  'Manipuri Literature'),
    ('marathi literature',  'Marathi Literature'),
    ('nepali literature',  'Nepali Literature'),
    ('oriya literature',  'Oriya Literature'),
    ('punjabi literature',  'Punjabi Literature'),
    ('sanskrit literature',  'Sanskrit Literature'),
    ('santhali literature',  'Santhali Literature'),
    ('sindhi literature',  'Sindhi Literature'),
    ('tamil literature', 'Tamil Literature'),
    ('telugu literature',  'Telugu Literature'),
    ('urdu literature',  'Urdu Literature'),
    ('english literature',  'English Literature')
        ]
    Name = serializers.CharField(max_length=30, required=False)
    Phone_number = serializers.CharField(max_length=20, required=False)
    Date_of_birth = serializers.DateField(required=False, allow_null=True)
    Num_of_Prelims=serializers.IntegerField(allow_null=True)
    Num_of_Mains=serializers.IntegerField(allow_null=True)
    Num_of_Interviews=serializers.IntegerField(allow_null=True)
    Rank_secured=serializers.BooleanField(allow_null=True)
    Medium = serializers.MultipleChoiceField(choices=medium)
    Profile_image = serializers.ImageField(required=False)
    Optional=serializers.CharField(allow_null=True)
    Role=serializers.CharField(allow_null=True)
    Evaluation_language=serializers.CharField(allow_null=True)
    Experience=serializers.CharField(required=False)
    Existing_std_email=serializers.EmailField(allow_null=True)
    assignment_checked=serializers.FileField(allow_null=True)
    marksheet=serializers.FileField(allow_null=True)

  
# Profile of Reviewer
class ReviewerSerializer(serializers.Serializer):
    MEDIUM_CHOICES = [
        ('english', 'English'),
        ('hindi', 'Hindi'),
    ]
    name = serializers.CharField(max_length=30, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    medium = serializers.ChoiceField(choices=MEDIUM_CHOICES, default='english')
    profile_image = serializers.ImageField( required=False)


# Profile of Enquiry
class EnquirySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    profile_image = serializers.ImageField( required=False)


# Profile of Admin
class AdminSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, required=False)
    profile_image = serializers.ImageField( required=False)


# Profile of Superuser
class SuperuserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, required=False)
    profile_image = serializers.ImageField( required=False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email']  # Include any other fields as needed

