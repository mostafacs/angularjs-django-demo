from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from accounts.UserSerializer import UserSerializer
from accounts.models import PresentUser
from django.contrib.auth import authenticate, login, logout
import json


class UserView(viewsets.ModelViewSet):

    queryset = PresentUser.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
def make_login(request):

        print('body =='+str(request.body))
        #print('body22 =='+str(request.raw_post_data))
        data = json.loads(request.body.decode('latin-1'))
        email = data["email"]
        password = data["password"]

        print(email)
        print(password)

        user = authenticate(username=email,
                                password=password)
        if not user :
            print('Return Not ACTIVEE....')
            return  HttpResponse('{ "message" : "Not Active User" }')
        else:
           # try:
                print('Login....')
                login(request, user)
                user_text = UserSerializer(request.user).data
                sessionid = request.session.session_key
                csrf = request.COOKIES.get('csrftoken')
                print('session ID = '+str(sessionid))
                print('CSRF = '+str(csrf))
                return JsonResponse({"user":user_text,"sessionid":sessionid})
        '''    except:
                print('Return Not Valid....')
                return HttpResponse( 'Not Valid Username and Password')
                '''
@csrf_exempt
def current_login(request):
    if request.user.is_authenticated():
        user_text = UserSerializer(request.user).data
        return JsonResponse(user_text)
    else:
        return JsonResponse({ "message" : "Not Login Yet!" })

