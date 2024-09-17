from rest_framework import serializers
from .models import Student
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
    #courseenroll = serializers.CharField(max_length=1000, required=False)
    
    def create(self, validated_data):
        # Handle the creation of a new Evaluator instance
        return Student.objects.create(**validated_data)
    class Meta:
        model = Student
        fields = '__all__'

    def update(self, instance, validated_data):
        # Update fields based on the validated data
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.medium = validated_data.get('medium', instance.medium)
        instance.attempt = validated_data.get('attempt', instance.attempt)
        # Save the updated instance
        instance.save()
        return instance