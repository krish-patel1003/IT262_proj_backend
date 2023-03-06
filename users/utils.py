from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'user_id': user.id,
        'email': user.email,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
