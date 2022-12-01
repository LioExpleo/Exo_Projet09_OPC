from django.shortcuts import render

# Create your views here.
# import de httpResponse
from django.http import HttpResponse



# retourner httpresponse avec comme balise HTML h1 qui contient le message Hello...
def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')
# Ensuite, associer cette vue à une adresse URL dans urls.py

def about(request):
    return HttpResponse('<h1>A propos</h1> <p> Nous adorons merch ! </p>')

def listings(request):
    return HttpResponse('<h1>Listing </h1> <p> Liste de ... pour exemple ! </p>')

def contact(request):
    return HttpResponse('<h1>Contact </h1> <p> Contact de ... pour exemple ! </p>')



def tchao1(request):
    return HttpResponse('<h1>tchao 0001!</h1>')
