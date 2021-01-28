import hashlib
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class UserItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined')


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Class to serialize data for user profile details
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'current_position', 'about', 'company', 'department', 'date_joined')


class UserSerializer(serializers.ModelSerializer):
    """
    Class to serialize data for user validation
    """
    first_name = serializers.CharField(max_length=60)
    last_name = serializers.CharField(max_length=60)
    current_position = serializers.CharField(max_length=64)
    about = serializers.CharField(max_length=255)
    class Meta:
        model = CustomUser
        fields = ('id', 'email','username', 'first_name', 'last_name',
                  'current_position', 'about', 'company', 'department','date_joined')
    def validate(self, data):
        if len(data['first_name']) + len(data['last_name']) > 60:
            raise serializers.ValidationError({
                'first_name': 'First + Last name should not exceed 60 chars'})
        return data

        
class UserRegistrationSerializer(serializers.Serializer):
    """
    Serializer for Registration - password match check
    """
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    def create(self, data):
        return CustomUser.objects.create_user(data['email'], data['password'])
    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError({
                'password': 'Please enter password and confirmation'})
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(
                {'password': 'Passwords don\'t match'})
        return data