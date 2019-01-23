from django.urls import path
from . import views

app_name = 'quest'
urlpatterns = [
    path('', views.index, name='index'),
    path('quest/questionario/', views.questionario, name='questionario'),
    path('quest/resultados/<int:quest_id>', views.resultados, name='resultados'),
    path('quest/votos/<int:quest_id>', views.votos, name='votos'),
]