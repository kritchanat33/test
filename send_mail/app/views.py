# Create your views here.

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app.models import ReplyMail
from .serializers import ReplyMailSer

from django.core.mail import send_mail

import re

def CheckEmail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex,email)

class ReplyMailView(APIView):
    # 2. Create
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = ReplyMail.objects.filter(user = request.user.id)
        serializer = ReplyMailSer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        
        data = {
            'email': request.data.get('email'), 
            'name': request.data.get('name'), 
            'message': request.data.get('message'),
            'sender_email': request.data.get('sender')
        }
        
        if CheckEmail(data['sender_email']) and  CheckEmail(data['email']):
            return Response('invalid email', status=status.HTTP_400_BAD_REQUEST)
        
        try:
            send_mail(
                subject = 'Reply Email',
                message = data['message'],
                from_email = data['sender_email'],
                recipient_list = [data['email'],],
                auth_user = '<username>',
                auth_password = '<password>',
                fail_silently = False,
            )
        except:
            Response('something wrong' ,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = ReplyMailSer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)