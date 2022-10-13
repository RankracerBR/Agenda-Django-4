from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao','usuario') #Mostra o titulo, data e hora no 'Core' Eventos
    list_filter = ('titulo','data_evento','usuario',)#sempre depois do list filter tem que ter virgula

admin.site.register(Evento, EventoAdmin)