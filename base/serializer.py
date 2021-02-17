from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Event

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id","_id","username","email", "name", "isAdmin"]

    def get__id(self,obj): #just to be consistent with _id
        return obj.id

    def get_isAdmin(self,obj): #just to be consistent with _id
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name # The attributes of the user object are defined in the django documentation.
        if name == '':
            name = obj.email
        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields = ["id","_id","username","email", "name", "isAdmin", "token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        # You can enter a list of parameters here if you what to send specific data
        # fields = ["names","description"]
        fields = '__all__' # to return back everything