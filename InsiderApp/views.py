from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from InsiderApp.models import InsiderTransaction


# It will be able to fetch only insider transactions all data based on symbol. Also,
# the result will include the average of the cost.
#  You will have to add filters here. Let’s say pass the parameter of cost in url. And
# make the filter on that value that returns all the rows, which have cost more
# than our parameter.


# It takes two parameters as symbol and cost above which average will be taken
@api_view(['GET'])
@csrf_exempt
def insider_detail(request, symb, costLimit):
    insider = InsiderTransaction.objects.filter(symbolKey__symbol=symb)
    if not insider.exists():
        return JsonResponse({'message': "No Insider Transaction found against this Symbol"})

    if request.method == 'GET':
        insider = list(
            InsiderTransaction.objects.filter(symbolKey__symbol=symb, cost__gte=costLimit).values("name").annotate(
                avg_cost=(Avg("cost"))))
        print(insider)
        context = {
            'result': insider
        }
        return JsonResponse(context)
