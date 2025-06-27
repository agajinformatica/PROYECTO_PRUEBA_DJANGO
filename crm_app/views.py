from django.shortcuts import render
from .models import Customer, Interaction
from django.db.models import Max, F
from datetime import datetime, timedelta
from django.utils.timezone import now
from django.db.models.functions import TruncDay
from django.db.models import Q

def crm_view(request):
    # Filtros por nombre y cumpleaños
    search = request.GET.get("search", "")
    birthday_filter = request.GET.get("birthday", "")  # puede ser "week"

    customers = Customer.objects.all()

    # Filtrar por nombre (ignora mayúsculas/minúsculas)
    if search:
        customers = customers.filter(full_name__icontains=search)

    # Filtrar por cumpleaños de esta semana
    if birthday_filter == "week":
        today = datetime.today()
        start_week = today - timedelta(days=today.weekday())
        end_week = start_week + timedelta(days=6)
        customers = customers.filter(birth_date__month=today.month, birth_date__day__gte=start_week.day, birth_date__day__lte=end_week.day)

    # Obtener última interacción por cliente
    customers = customers.annotate(
        last_interaction_date=Max('interaction__interaction_date'),
        last_interaction_type=F('interaction__interaction_type')
    )

    # Ordenamiento
    sort = request.GET.get("sort", "")
    if sort in ["name", "company", "birthday", "interaction"]:
        if sort == "name":
            customers = customers.order_by("full_name")
        elif sort == "company":
            customers = customers.order_by("company__name")
        elif sort == "birthday":
            customers = customers.order_by("birth_date")
        elif sort == "interaction":
            customers = customers.order_by("-last_interaction_date")

    context = {
        "customers": customers,
        "now": now()
    }
    return render(request, "crm_app/crm_view.html", context)
