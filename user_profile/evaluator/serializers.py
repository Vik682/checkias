from rest_framework import serializers
from .models import Evaluator



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
        # Handle the creation of a new Evaluator instance
        return Evaluator.objects.create(**validated_data)
    class Meta:
        model = Evaluator
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
