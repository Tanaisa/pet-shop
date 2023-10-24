from django.core.management.base import BaseCommand
from model_bakery import baker
from reserva.models import Reserva

class command(BaseCommand):
    help = 'Cria dados fakes para testar a API de agendamento'
    
    def handle(self, *args, **options):
        total= 50
        self.stdout.write(
            self.style.WARNING(f'criando{total} argumentos')
        )
        for i in range(total):
            reserva = baker.make(Reserva)
            reserva.save()
            self.stdout.write(
                self.style.SUCCESS('agedamentos criados')
            )