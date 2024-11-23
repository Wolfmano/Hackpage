from django.shortcuts import render, get_object_or_404, redirect
from assistant.models import Ticket,Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from assistant.forms import TicketForm


@login_required
def profile_ticket_list(request):
    user = request.user
    tickets = Ticket.objects.all()  # Изначально получаем все тикеты
    category_id = request.GET.get('category')

    # Фильтруем по категории, если она указана
    if category_id:
        tickets = tickets.filter(category_id=category_id)

    # Исключаем закрытые тикеты
    tickets = tickets.exclude(status='closed')

    categories = Category.objects.all()

    # Разделяем логику для роли "mentor" и "student"
    if user.role == "mentor":
        print(user.role)
        return render(request, 'ticket_mentor.html', {'tickets': tickets, 'categories': categories})
    elif user.role == "student":
        return render(request, 'user_ticket.html', {'tickets': tickets, 'categories': categories})


def close_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.status = 'closed'
        ticket.save()
        messages.success(request, f"Тикет '{ticket.title}' успешно закрыт.")
    return redirect('profile_ticket_list')
#
# def create_ticket(request):
#     def ticket_create(request):
#         if request.method == 'POST':
#             form = TicketForm(request.POST)
#             if form.is_valid():
#                 ticket = form.save(commit=False)
#                 if request.user.is_authenticated:
#                     ticket.author = request.user  # Привязываем автором текущего пользователя
#                 ticket.save()
#                 return redirect('index')  # Или другая страница
#         else:
#             form = TicketForm()
#         return render(request, 'create.html', {'form': form})


# def create_ticket(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             ticket = form.save(commit=False)  # Создаем объект тикета, но не сохраняем еще в базу
#             category_id = form.cleaned_data['category']  # Получаем ID категории из формы
#             category = Category.objects.get(id=category_id)  # Получаем объект категории по ID
#             ticket.category = category  # Присваиваем объект Category в поле category
#             ticket.save()  # Сохраняем тикет в базе данных
#             return redirect('profile_ticket_list')  # Перенаправляем после успешного создания тикета
#     else:
#         form = TicketForm()
#     return render(request, 'create.html', {'form': form})


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)  # Сохраняем объект тикета, но не сохраняем в базу
            ticket.author = request.user  # Привязываем автором текущего пользователя (если необходимо)
            ticket.save()  # Сохраняем тикет в базу данных
            return redirect('profile_ticket_list')  # Перенаправляем после успешного создания тикета
    else:
        form = TicketForm()
    return render(request, 'create.html', {'form': form})
# Create your views here.
