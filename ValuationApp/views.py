from django.db.models import ExpressionWrapper, F, FloatField
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from ValuationApp.models import Valuation


# Create your views here.

# Task that  will fetch the data from valuation table for AAPL, and it will also return the
# market cap per share. (market cap / price)
@api_view(['GET'])
@csrf_exempt
def valuation_detail(request, symb):
    val = Valuation.objects.filter(symbol_key__symbol=symb)
    if not val.exists():
        return JsonResponse({'message': "No Valuation record  found against this Symbol"})

    if request.method == 'GET':
        val = (Valuation.objects.filter(symbol_key__symbol=symb).values('market_cap', 'pe_ratio',
                                                                        'symbol_key__price').annotate(
            per_capita=ExpressionWrapper(F('market_cap') / F('symbol_key__price'), output_field=FloatField())))
        print(val)
        context = {
            'result': list(val.values())
        }
        return JsonResponse(context, safe=False)
