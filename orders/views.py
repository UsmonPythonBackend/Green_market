from django.shortcuts import render

def card(request):
    return render(request, 'cart.html')