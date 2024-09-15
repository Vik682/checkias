from authentication.models import  UserToken
from rest_framework import authentication
from rest_framework import exceptions


class UserAuthenticationBackend(authentication.TokenAuthentication):

    keyword = 'idToken'
    model = UserToken

    def authenticate_credentials(self, token):
        try:
            decoded_token = UserToken.objects.get(key=token)
        except UserToken.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        try:
            user = decoded_token.user

        except Exception:
            raise exceptions.AuthenticationFailed('No such user exists')

        # allow users to make API calls only after profile is completed
        return (user, decoded_token)