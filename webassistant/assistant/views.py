from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import TicketForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket, Category

def index(request):
    return render(request,"index.html")

from django.shortcuts import render, redirect
from .forms import TicketForm

def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            if request.user.is_authenticated:
                ticket.author = request.user  # Привязываем автором текущего пользователя
            ticket.save()
            return redirect('index')  # Или другая страница
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})