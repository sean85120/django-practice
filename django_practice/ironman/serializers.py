from rest_framework import serializers
from .models import People

class People2Serializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

class PeopleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    power = serializers.BooleanField()
    bio = serializers.CharField(max_length=200)

    def validate_date(self):
        if self.age < 0:
            raise serializers.ValidationError("Age must be bigger than 0!")


from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password],
                                     style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(write_only=True, required=True)
    phone = serializers.CharField(min_length=8, max_length=10, write_only=True)
    organization = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'phone', 'organization')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        userprofile = UserProfile.objects.create(
            user=user,
            phone=validated_data['phone'],
            organization=validated_data['organization'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


# login
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label = 'Username',
        write_only = True
    )

    password = serializers.CharField(
        label = 'Password',
        style = {'input_type': 'password'},
        trim_whitespace = False,
        write_only = True,
    )
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
                user = authenticate(request=self.context['request'], username=username, password=password)
                
                if not user:
                    msg = {
                        'success': False,
                        'message': 'Wrong username or password'
                    }
                    raise serializers.ValidationError(msg)
        else:
            msg = {
                'success': False,
                'message': 'Username and password are required'
            }
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs


from .models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'