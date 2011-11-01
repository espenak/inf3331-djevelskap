from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Delivery
from django.core import serializers
import json

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



def restful_delivery(request, id=None):
    if request.method == 'GET':
        if id == None:
            jsondata = serializers.serialize("json", Delivery.objects.all())
        else:
            delivery = Delivery.objects.get(id=id)
            deliverydict = dict(id=delivery.id,
                                user=delivery.user,
                                contents=delivery.contents,
                                feedback=delivery.feedback)
            jsondata = json.dumps(deliverydict)
        return HttpResponse(jsondata, content_type='text/plain')
    elif request.method == 'POST':
        pass # TODO
    elif request.method == 'PUT':
        pass # TODO
    elif request.method == 'DELETE':
        pass # TODO
