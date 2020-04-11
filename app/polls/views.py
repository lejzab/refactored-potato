from django.http import HttpResponse

def index(request):
    return HttpResponse('witaj świecie index polls')