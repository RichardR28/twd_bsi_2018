from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango diz olá pessoal!")
