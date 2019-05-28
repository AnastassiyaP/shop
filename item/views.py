from django.http import JsonResponse

from .models import get_items, get_user_boughts


def items(request):
    sex = request.GET.get('sex')
    price = request.GET.get('price')
    return JsonResponse(
        list(get_items(sex=sex, price=price).values()),
        safe=False
    )

def user_boughts(request):
    id = request.GET.getlist('id')
    return JsonResponse(
        list(get_user_boughts(id=id).values()),
        safe=False
    )
