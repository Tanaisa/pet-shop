from django import forms 
from reserva.models import Reserva

# Data com calendário
class DateInput(forms.DateInput):
    input_type = 'date'


# Formulário de reserva
class ReservaForm(forms.ModelForm):
    class Meta: # Metadados do model
        # Definir o modelo base
        model = Reserva
        # Definir os campos do formulário
        fields = ['nome_pet', "telefone", "data_reserva", "observacoes"]

        # Definir os widgets
        widgets = {
            'nome_pet': forms.TextInput(
                attrs={
                    'placeholder': 'Insira nome do seu pet'
                }
            ),    
            'telefone': forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu telefone'
                }
            ),
            'data_reserva': DateInput(),
            'observacoes': forms.Textarea(
                attrs={
                    'placeholder': 'Insira suas observações'
                }
            )
        }

        # Definir as labels dos campos
        labels = {
            'nome_pet': 'Nome do Pet:',
            'telefone': 'Telefone:',
            'data_reserva': 'Data de Reserva do Banho:',
            'observacoes': 'Observações:'
        }