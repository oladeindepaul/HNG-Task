from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getdata(request):
    person = {"slackusername" : "Paul", "backend" : True, "age" : "21", "bio" : "Hello, i'm Oladeinde paul . A backend developer and a lover of football"}
    return Response(person)