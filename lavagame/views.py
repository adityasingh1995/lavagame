from django.http import HttpResponse
from django.shortcuts import redirect
def game(request):
    return redirect('/static/game.html')
    


