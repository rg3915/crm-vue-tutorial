from django.http import JsonResponse
from django.contrib.auth.models import User


def customers(request):
    items = User.objects.all()
    data = [
        {
            'first_name': item.first_name,
            'last_name': item.last_name,
        }
        for item in items
    ]
    response = {'data': data}
    return JsonResponse(response)
