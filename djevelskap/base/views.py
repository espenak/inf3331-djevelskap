from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Delivery
#import json

def helloworld(request):
    return HttpResponse('Hello world', content_type='text/plain')

def list_all(request):
    out = ''
    for delivery in Delivery.objects.all():
        #out += '{user:>20}:{assignment}\n'.format(user=delivery.user, assignment=delivery.assignment)
        out += '{user:>20}:{assignment}\n'.format(**delivery.__dict__)

    #out = []
    #for delivery in Delivery.objects.all():
        #out.append({'user': delivery.user})
    #return HttpResponse(json.dumps(out), content_type='text/plain')

def list_all_tpl(request):
    deliveries = Delivery.objects.all() # vanligvis mange linjer!
    return render_to_response('list-all.django.html',
                              {'deliveries': deliveries})
