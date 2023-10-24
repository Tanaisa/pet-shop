from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 

class Command (BaseCommand):
    help = 'cria um novo token para ser usado'
    
    def add_arguments(self, parser):
        parser.add_argument('..username', required=True)
        parser.add_argument('..password', required=True)
        
    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        self.stdout.white(
            self.style.WARNING(f'Criando Usuario com o nome (username)')
            
        )
        user = User(username=username)
        user.first_name = username
        user.save()
        self.stdout.white(
            self.style.SUCCESS('Usuário criado com sucesso!')
        )
        self.stdout.white(
            self.style.WARNING('Criando token para o usuário')
        )
        token = Token.objects.create(user=user)
        self.stdout.white(
            self.style.SUCCESS(f'Token para usuário: {token.key}')
     )