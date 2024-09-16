from rest_framework import serializers
from django.contrib.auth import get_user_model
from user_profile.models import EvaluatorModel

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
    Name = serializers.CharField(max_length=50,required=False)
    date_of_birth = serializers.DateField(required=False)
    Phone_number = serializers.IntegerField(required=False,default=0)
    Num_of_Prelims=serializers.IntegerField(required=False,default=0)
    Num_of_Mains=serializers.IntegerField(required=False,default=0)
    Num_of_Interviews=serializers.IntegerField(required=False,default=0)
    profile_picture = serializers.ImageField(required=False)
    Rank_secured=serializers.BooleanField(default=False)
    Medium = serializers.CharField(default='english')
    Optional=serializers.CharField(default='Not Selected')
    Role=serializers.CharField(required=False)
    Evaluation_language=serializers.CharField(required=False)
    Experience=serializers.CharField(required=False)
    Existing_std_email=serializers.EmailField(required=False)
    assignment_checked=serializers.FileField(required=False)
    marksheet=serializers.FileField(required=False)
    
    def create(self, validated_data):
        # Handle the creation of a new EvaluatorModel instance
        return EvaluatorModel.objects.create(**validated_data)
    class Meta:
        model = EvaluatorModel
        fields = '__all__'

    def update(self, instance, validated_data):
        # Update fields based on the validated data
        instance.Name = validated_data.get('Name', instance.Name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.Phone_number = validated_data.get('Phone_number', instance.Phone_number)
        instance.Num_of_Prelims = validated_data.get('Num_of_Prelims', instance.Num_of_Prelims)
        instance.Num_of_Mains = validated_data.get('Num_of_Mains', instance.Num_of_Mains)
        instance.Num_of_Interviews = validated_data.get('Num_of_Interviews', instance.Num_of_Interviews)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.Rank_secured = validated_data.get('Rank_secured', instance.Rank_secured)
        instance.Medium = validated_data.get('Medium', instance.Medium)
        instance.Optional = validated_data.get('Optional', instance.Optional)
        instance.Role = validated_data.get('Role', instance.Role)
        instance.Evaluation_language = validated_data.get('Evaluation_language', instance.Evaluation_language)
        instance.Experience = validated_data.get('Experience', instance.Experience)
        instance.Existing_std_email = validated_data.get('Existing_std_email', instance.Existing_std_email)
        instance.assignment_checked = validated_data.get('assignment_checked', instance.assignment_checked)
        instance.marksheet = validated_data.get('marksheet', instance.marksheet)
        # Save the updated instance
        instance.save()
        return instance
class UserSerializer(serializers.Serializer):
    email=serializers.EmailField()

 
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
