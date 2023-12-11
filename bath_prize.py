import random
from django.core.management.base import BaseCommand

from reserva.models import Petshop, Reserva

class Command(BaseCommand):
    def list_petshops(self):
        return Petshop.objects.all().values_list('pk', flat=True)
    
    def escolher_reservas(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
         quantidade = len(banhos_list)
    
         return random.sample(banhos_list, quantidade)
     
    def imprimir_info_petshop(self, petshop):
            self.stdout.write(
                self.style.HTTP_INFO(
                    'Dados do petshop que realizar o sorteio'
                    )
                )
            self.stdout.write(f'Nome do Petshop:{petshop.nome}')
            self.stdout.write(
                f'Enderenço: {petshop.rua}. {petshop.numero }- {petshop.bairro}'
            )
    def add_arguments(self, parser):
        parser.add_argument(
            'quantity',
            nargs='?',
            default=5,
            type=int,
            help='Quantidade de reservas que deverão ser sorteadas'
            )
        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.list_petshops(),
            help='ID do petshop para selecionar as reservas'
            )
    def handle(self, *args, **options):
        quantity = options['quantity']
        petshop_id = options['petshop']

        petshop = Petshop.objects.get(pk=petshop_id)
        reservas = Reserva.objects.filter(petshop=petshop_id)
        
        banhos_escolhidos = self.escolher_reservas(reservas, quantity)

        self.stdout.write(
                self.style.SUCCESS('sorteio concluido')
            )
        
        self.imprimir_info_petshop(petshop)
        self.imprimir_reservas_sorteadas(banhos_escolhidos) 
        
    def imprimir_reservas_sorteadas(self, reservas):
        self.stdout.write()
        self.stdout.write(
         self.style.HTTP_INFO('Dados dos animais sorteados')
        )

        self.stdout.write(
        self.style.HTTP_INFO('=' * 35)
        )

        for reserva in reservas:
            self.stdout.write(f'Animal: {reserva.nome_pet}')
            self.stdout.write(f'Telefone do Tutor: {reserva.telefone}')

            self.stdout.write(
                self.style.HTTP_INFO('=' * 35)
            ) 