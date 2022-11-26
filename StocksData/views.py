from django.http import JsonResponse
import requests

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view

from StocksData.Serializer import StockDataSearilizer, StockDataSearilizerForPOST
from StocksData.models import Stocks


# You will fetch the 10 rows of insider transaction table, and the related data of
# valuation table using just one call on the stock table using symbol. Serializer

@api_view(['GET'])
@csrf_exempt
def stocks_detail(request, symb):
    try:
        stocks = Stocks.objects.get(symbol=symb)
    except Stocks.DoesNotExist:
        return JsonResponse({'message': "No Stock Found"})

    if request.method == 'GET':
        sd = StockDataSearilizer(stocks)
        context = {
            'result': sd.data
        }
        return JsonResponse(context)


# Write the post API to save data in the stock table and insider transactions table. Searilizer
@api_view(['POST'])
@csrf_exempt
def stocks_detail(request):
    if request.method == 'POST':
        print(request.data)

        data_serializer = StockDataSearilizerForPOST(data=request.data, many=True)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=status.HTTP_201_CREATED, safe=False)
        print(data_serializer.errors)
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


# Test View to Insert data POST request
def post_data(request):
    url = 'http://127.0.0.1:8000/Stocks/MainApi/'

    data = [{
        'symbol': 'APPKTR',
        'name': 'APPOLPOST',
        'price': 23,
        'change': 45,
        'symbolKey': {

            'name': 'APPOLPOST',
            'cost': 34

        }
    }]

    # sending post request and saving response as response object

    r = requests.post(url=url, json=data)

    return JsonResponse(r.text, safe=False)
