from django.shortcuts import render, get_object_or_404
from .models import Update

def allUpdates(request):
    updates = Update.objects.order_by('-pub_date')
    return render(request, 'updates/updates.html', {'updates': updates})

def updateDetail(request, update_id):
    update = get_object_or_404(Update, pk=update_id)
    return render(request, 'updates/updatedetail.html', {'update': update})
