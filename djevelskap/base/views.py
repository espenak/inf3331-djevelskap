from django.http import HttpResponse
from models import Delivery

def helloworld(request):
    return HttpResponse('Hello world', content_type='text/plain')

def list_all(request):
    out = ''
    for delivery in Delivery.objects.all():
        out += '{user}:{assignment}\n'.format(user=delivery.user, assignment=delivery.assignment)
    return HttpResponse(out, content_type='text/plain')
