from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from ..db_utils import manager as db_manager 

def config(request):
    params_with_values = db_manager.get_configurations()
    return render(request, 'client/config.html', {'params_with_values': params_with_values})

def get_configurations(request):
    """
    Récupère les nom des paramètres de configuration et leurs valeurs possibles associées.
    """
    configurations = db_manager.get_configurations()
    return JsonResponse(configurations, safe=False)



    