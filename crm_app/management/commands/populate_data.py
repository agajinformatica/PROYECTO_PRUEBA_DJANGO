from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random
from crm_app.models import User, Company, Customer, Interaction

fake = Faker()

class Command(BaseCommand):
    help = "Populate database with sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("⚙️ Populating database...")

        # Crear 3 usuarios
        users = []
        for i in range(3):
            user = User.objects.create_user(
                username=f'user{i+1}',
                email=f'user{i+1}@test.com',
                password='123456',
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )
            users.append(user)
        self.stdout.write("✅ 3 usuarios creados")

        # Crear 10 compañías
        companies = []
        for _ in range(10):
            companies.append(Company.objects.create(name=fake.company()))
        self.stdout.write("✅ 10 compañías creadas")

        # Crear 1000 clientes distribuidos
        customers = []
        for _ in range(1000):
            customer = Customer.objects.create(
                full_name=fake.name(),
                birth_date=fake.date_of_birth(minimum_age=20, maximum_age=70),
                company=random.choice(companies),
                representative=random.choice(users)
            )
            customers.append(customer)
        self.stdout.write("✅ 1000 clientes creados")

        # Crear 500 interacciones por cliente
        interaction_types = ['Call', 'Email', 'SMS', 'Facebook', 'WhatsApp']
        interactions_bulk = []
        for idx, customer in enumerate(customers):
            for _ in range(500):
                interactions_bulk.append(Interaction(
                    customer=customer,
                    interaction_type=random.choice(interaction_types),
                    interaction_date=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
                ))
            if (idx + 1) % 50 == 0:
                self.stdout.write(f"⏳ Procesando cliente {idx+1}/1000")

        Interaction.objects.bulk_create(interactions_bulk, batch_size=10000)
        self.stdout.write("✅ 500,000 interacciones creadas")

        self.stdout.write(self.style.SUCCESS("🎉 Datos de prueba creados con éxito"))
