from api.models import User
from django.contrib.auth.backends import BaseBackend

class PhoneAuthBackEnd(BaseBackend):

    def authenticate(self, request, username, password, **kwargs):
        
        try:

            user=User.objects.get(phone=username)

            if user.check_password(password):

                return user
            
            else:

                return None
            
        except:

            return None

    def get_user(self, user_id):

        try:

            return User.objects.get(pk=user_id)

        except:

            return None