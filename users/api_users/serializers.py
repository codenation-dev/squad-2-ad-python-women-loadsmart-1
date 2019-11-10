from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']
        """We need to tell the web browser that the password field should not
        be read
        """
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # def save(self):
    #     """The 'validated_data' becomes available when the data is
    #         validated during the request
    #     """
    #     user = CustomUser(
    #         email=self.validated_data['email'],
    #     )
