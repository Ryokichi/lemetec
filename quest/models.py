from django.db import models

class Questionario(models.Model):
    titulo = models.CharField(max_length=100)
    qtd_respondida = models.IntegerField(default=0)
    def __str__(self):
        return "id:"+str(self.pk) + " - " + self.titulo

class Pergunta(models.Model):
    questionario_id = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    img_nome = models.CharField(max_length=100)
    def __str__(self):
        return "id:"+str(self.pk)+" - "+self.texto

class Resposta(models.Model):
    pergunta_id = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return "id:"+str(self.pk)+"|pai:"+str(self.pergunta_id)+" - "+self.texto   
    
    