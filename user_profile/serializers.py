from rest_framework import serializers

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
    MEDIUM_CHOICES = [
        ('english', 'English'),
        ('hindi', 'Hindi'),
    ]
    name = serializers.CharField(max_length=30, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    medium = serializers.ChoiceField(choices=MEDIUM_CHOICES, default='english')
    profile_image = serializers.ImageField( required=False)

  
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
