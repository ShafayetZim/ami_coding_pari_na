from django.shortcuts import render
from .models import InputValue
import json
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status


def khoj_search(request):
    if request.method == 'POST':
        input_values = request.POST.get('input_values')
        search_value = request.POST.get('search_value')
        input_values_list = [int(x.strip()) for x in input_values.split(',')]
        input_values_list.sort(reverse=True)
        input_values_str = ', '.join(str(x) for x in input_values_list)

        InputValue.objects.create(user=request.user, input_values=input_values_str)

        is_search_value_found = int(search_value) in input_values_list

        return render(request, 'khoj_search.html', {'is_search_value_found': is_search_value_found})

    return render(request, 'khoj_search.html')


@api_view(['POST'])
def get_input_values_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            start_datetime_str = data.get('start_datetime')
            end_datetime_str = data.get('end_datetime')
            user_id = data.get('user_id')

            start_datetime = timezone.datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M:%S')
            end_datetime = timezone.datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M:%S')

            input_values = InputValue.objects.filter(
                user_id=user_id,
                timestamp__range=(start_datetime, end_datetime)
            )

            payload = []
            for iv in input_values:
                payload.append({
                    'timestamp': iv.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'input_values': iv.input_values,
                })

            response_data = {
                'status': 'success',
                'user_id': user_id,
                'payload': payload,
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

