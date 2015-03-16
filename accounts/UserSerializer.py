from accounts.models import PresentUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'mobile_number', 'gender')
        write_only_fields = ('password',)

