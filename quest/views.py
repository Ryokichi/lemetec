from django.http      import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template  import loader
from django.urls      import reverse
from .models          import Questionario, Pergunta, Resposta

def index(request):
    template = loader.get_template('quest/index.html')
    output = {
        'questionario' : 'quest/questionario/',
        'resultados' : 'quest/resultados/1',
    }
    return HttpResponse(template.render(output, request))


def questionario(request, questId = 1):
    template = loader.get_template('quest/questionario.html')   
    output = {
        'questionario' : Questionario.objects.get(id = questId),
    }
    return HttpResponse(template.render(output, request))


def resultados(request, quest_id):    
    template     = loader.get_template('quest/resultados.html')
    questionario = Questionario.objects.get(id = quest_id)
    perguntas    = Pergunta.objects.filter(questionario_id = quest_id)
    perg_resp    = []

    for p in perguntas:
        perg_id = p.id
        resp_id = None
        maior_voto = 0

        for r in Resposta.objects.filter(pergunta_id = perg_id):
            if r.votos > maior_voto:
                resp_id = r.id
                maior_voto = r.votos

        perg_resp.append(
            {
                'pergunta' : Pergunta.objects.get(id=perg_id),
                'resposta' : Resposta.objects.get(id=resp_id)
            }
        )
        
        print(perg_resp)

    output = {
        'questionario' : questionario,
        'perguntas'    : perguntas,
        'perg_resp'    : perg_resp,
    }
    return HttpResponse(template.render(output, request))


def votos(request, quest_id):
    msg_erro = "Houve um erro ao processar os dados recebidos"
    houve_falha = False
    questionario = get_object_or_404(Questionario, id=quest_id)
    
    #Limpa os dados do banco
    '''
    questionario.qtd_respondida = 0
    questionario.save()
    for r in Resposta.objects.all():
        r.votos = 0
        r.save()
    '''

    try:
        perguntas = Pergunta.objects.filter(questionario_id = quest_id)
        resp_id = None
        for p in perguntas:            
            perg_id = 'perg_'+str(p.id)
            try:
                resp_id = request.POST[perg_id]                
            except:
                houve_falha = True
                msg_erro = "Nem todas as perguntas foram respondidas <br>"+p.texto

        if not (houve_falha):
            questionario.qtd_respondida += 1
            questionario.save()

            for p in perguntas:
                perg_id = 'perg_'+str(p.id)
                resp_id = request.POST[perg_id]
                resposta = Resposta.objects.get(id = resp_id)
                resposta.votos += 1
                resposta.save()
                

    except(KeyError, Questionario.DoesNotExist):
        return HttpResponse("Exception error")
    else:
        if (houve_falha):
            return HttpResponse(msg_erro)
        else:
            return HttpResponseRedirect(reverse('quest:resultados', args=(quest_id,)))
