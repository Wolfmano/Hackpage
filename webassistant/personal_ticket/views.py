from django.shortcuts import render, get_object_or_404, redirect
from assistant.models import Ticket,Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from assistant.forms import TicketForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Message


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
import json


@login_required
def profile_ticket_list(request):
    user = request.user
    tickets = Ticket.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        tickets = tickets.filter(category_id=category_id)

    tickets = tickets.exclude(status='closed')

    categories = Category.objects.all()
    if user.role == "mentor":
        print(user.role)
        return render(request, 'ticket_mentor.html', {'tickets': tickets, 'categories': categories})
    elif user.role == "student":
        tickets = Ticket.objects.filter(author=user, status__in=['open', 'in_progress']) 
        if category_id:
            tickets = tickets.filter(category_id=category_id)
        
        open_ticket_count = Ticket.objects.filter(author=user, status__in=['open', 'in_progress']).count()
        can_create_ticket = open_ticket_count < 3

        context = {
            'tickets': tickets,
            'categories': categories,
            'can_create_ticket': can_create_ticket,
            'open_ticket_count': open_ticket_count,
        }
        return render(request, 'user_ticket.html', context)


def close_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.status = 'closed'
        ticket.save()
    return redirect('profile_ticket_list')



def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            return redirect('profile_ticket_list')
    else:
        form = TicketForm()
    return render(request, 'create.html', {'form': form})





from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Message
from .forms import MessageForm
from django.http import JsonResponse

def ticket_detail_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    messages = ticket.messages.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.ticket = ticket
            message.user = request.user
            message.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'message': message.text,
                    'user': message.user.username,
                    'created_at': message.created_at.strftime('%d.%m.%Y %H:%M'),
                })
            else:
                return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = MessageForm()

    return render(request, 'message_ticket.html', {'ticket': ticket, 'messages': messages, 'form': form})