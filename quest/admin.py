from django.contrib import admin
from .models        import Questionario, Pergunta, Resposta

admin.site.register(Questionario)
admin.site.register(Pergunta)
admin.site.register(Resposta)