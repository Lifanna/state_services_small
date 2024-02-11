from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    return render(request, 'main/index.html')


def users_list(request):
    return render(request, 'main/users_list.html')


def business(request):
    notifications = models.Letter.objects.all()

    debt = models.Debt.objects.first()

    return render(request, 'main/business.html', context={
        'notifications': notifications,
        'debt': debt,
    })


def notification(request, id):
    notification = get_object_or_404(models.Letter, pk=id)

    return render(request, 'main/notification.html', context={
        'notification': notification,
    })
