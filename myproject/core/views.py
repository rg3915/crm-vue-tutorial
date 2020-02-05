from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def customers(request):
    items = User.objects.all()
    data = [
        {
            'username': item.username,
            'first_name': item.first_name,
            'last_name': item.last_name,
            'email': item.email,
        }
        for item in items
    ]
    response = {'data': data}
    return JsonResponse(response)


@csrf_exempt
def customer_create(request):
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    data = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    response = {'data': data}
    return JsonResponse(response)
