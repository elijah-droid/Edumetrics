from django.shortcuts import render
from .models import BroadCast
from django.http import JsonResponse


def to_broadcast(request):
    broadcasts = BroadCast.objects.filter(Done=False)
    if broadcasts.count() >= 1:
        br = broadcasts.last()
        br.Done = True
        br.save()

        data = {
            'message': br.Message,
            'numbers': ['0'+str(p.Tel) for p in br.Parents.all() if p.Tel],
        }
        
        # Return JSON response
    else:
        data = {
            'message': None
        }
    return JsonResponse(data)