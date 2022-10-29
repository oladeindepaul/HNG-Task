from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def getdata(request, *args, **kwargs):
    header = {"Access-Control-Allow-Origin":"*"}
    person = {"slackUsername" : "Oladeinde Paul", "backend" : True, "age" : 21, "bio" : "Hello, i'm Oladeinde paul . A backend developer and a lover of football"}
    return JsonResponse(person, headers = header)