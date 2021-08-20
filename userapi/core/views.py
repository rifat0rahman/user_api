from .serializers import UserSerializer
from .models import user
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def home(request):
    routes = {
        'users':'http://127.0.0.1:8000/users',
        'create_user':'http://127.0.0.1:8000/create_user'
    }
    return Response(routes)




# get all users here
@api_view(['GET'])
def users(request):
    users = user.objects.all()
    serializers = UserSerializer(users,many=True)
    return Response(serializers.data)



# post user here
@api_view(['POST'])
def create_user(request):

    if request.method == 'POST':
        data = request.data
        name = data['name']
        email = data['email']
        phone = data['phone']
        password = data['password']
        gender = data['gender']

        users = user.objects.create(
            name = name,
            email = email,
            phone = phone,
            password = password,
            gender = gender
        )

        country = None
        try:
            country = data['country']
            users.country = country
        except:
            pass

        state = None
        try:
            state = data['state']
            users.state = state
        except:
            pass

        dob = None
        try:
            dob = data['dob']
            users.dob = dob
        except:
            pass


        about = None
        try:
            about = data['about']
            users.about = about
        except:
            pass

        height = None
        try:
            height = data['height']
            users.height = height
        except:
            pass

        hobbies = None
        try:
            hobbies = data['hobbies']
            users.hobbies = hobbies
        except:
            pass


        alcohol = False
        try:
            alcohol = data['alcohol']
            users.alcohol = alcohol
        except:
            pass

        smoke = False
        try:
            smoke = data['smoke']
            users.smoke = smoke
        except:
            pass

        relationship = None
        try:
            relationship = data['relationship']
            users.relationship = relationship
        except:
            pass

        languages = None
        try:
            languages = data['languages']
            users.languages = languages
        except:
            pass
        
        users.save()

        return Response('new user has been inserted')