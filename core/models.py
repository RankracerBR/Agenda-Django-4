from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)#blank=true(fica branco)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)#auto_now irá inserir a hora exata de um determinado registro
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # O models.cascade irá além de excluir o usuário ele vai excluir todos os eventos do mesmo
    
    class Meta: #ao ivés no sqlmigrate mostrar o core_evento, ele irá só mostrar 'evento'
        db_table = 'evento'
    
    def __str__(self):
        return self.titulo #irá converter o nome event.object para o nome do titulo
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%MHrs')