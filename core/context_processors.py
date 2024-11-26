from django.contrib.auth.models import User

def current_user(request):
    return {'user': request.user}
